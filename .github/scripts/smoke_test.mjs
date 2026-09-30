// Smoke-test the built site in a real browser before it deploys.
//
//   node .github/scripts/smoke_test.mjs [site-dir]      (default: _site)
//
// Serves the built site locally, opens every page in sitemap.xml (plus the
// 404 page) in headless Chromium, and fails if any page:
//   - throws a JavaScript error, or logs a console error from site code
//   - requests a same-origin file that is missing (e.g. a CSV a script fetches)
//   - links to a same-origin page that does not exist
// External problems (a CDN timing out, a slow third-party host) are reported
// as warnings only, so a flaky third party can't block a deploy; an external
// resource that returns 404/410 still fails, since that is a broken URL.

import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import { chromium } from 'playwright';

const ROOT = path.resolve(process.argv[2] || '_site');
const PORT = 4789;
const ORIGIN = `http://localhost:${PORT}`;
const SITE_URL = 'https://hiyata.github.io';

const TYPES = {
  '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.json': 'application/json',
  '.csv': 'text/csv', '.xml': 'application/xml', '.svg': 'image/svg+xml', '.png': 'image/png',
  '.jpg': 'image/jpeg', '.webp': 'image/webp', '.ico': 'image/x-icon', '.webm': 'video/webm',
  '.pdb': 'text/plain', '.woff2': 'font/woff2', '.txt': 'text/plain',
};

// Mirrors GitHub Pages: /dir/ -> /dir/index.html, /page -> /page.html.
function resolveFile(urlPath) {
  const clean = decodeURIComponent(urlPath.split('?')[0]);
  const base = path.join(ROOT, clean);
  if (!base.startsWith(ROOT)) return null;
  for (const candidate of [base, path.join(base, 'index.html'), base + '.html']) {
    if (fs.existsSync(candidate) && fs.statSync(candidate).isFile()) return candidate;
  }
  return null;
}

const server = http.createServer((req, res) => {
  const file = resolveFile(req.url);
  if (!file) {
    res.writeHead(404, { 'content-type': 'text/html' });
    return res.end(fs.readFileSync(path.join(ROOT, '404.html')));
  }
  const size = fs.statSync(file).size;
  const type = TYPES[path.extname(file)] || 'application/octet-stream';
  const range = /bytes=(\d*)-(\d*)/.exec(req.headers.range || '');
  if (range) { // video players ask for byte ranges
    const start = range[1] ? +range[1] : 0;
    const end = range[2] ? +range[2] : size - 1;
    res.writeHead(206, { 'content-type': type, 'accept-ranges': 'bytes',
      'content-range': `bytes ${start}-${end}/${size}`, 'content-length': end - start + 1 });
    return fs.createReadStream(file, { start, end }).pipe(res);
  }
  res.writeHead(200, { 'content-type': type, 'content-length': size, 'accept-ranges': 'bytes' });
  fs.createReadStream(file).pipe(res);
});

const sitemap = fs.readFileSync(path.join(ROOT, 'sitemap.xml'), 'utf8');
const pages = [...sitemap.matchAll(/<loc>([^<]+)<\/loc>/g)]
  .map((m) => m[1].replace(SITE_URL, '') || '/')
  .concat('/404.html');

const failures = [];
const warnings = [];
const linkTargets = new Map(); // same-origin href path -> first page that links to it
const isLocal = (u) => u.startsWith(ORIGIN);

await new Promise((r) => server.listen(PORT, r));
const browser = await chromium.launch();

for (const pagePath of pages) {
  const context = await browser.newContext();
  const page = await context.newPage();
  const fail = (msg) => failures.push(`${pagePath}: ${msg}`);
  const warn = (msg) => warnings.push(`${pagePath}: ${msg}`);

  page.on('pageerror', (e) => fail(`JS error: ${e.message.split('\n')[0]}`));
  page.on('console', (m) => {
    if (m.type() !== 'error') return;
    const where = m.location().url || '';
    // A 4xx is reported again (with its URL) by the response handler below.
    if (/Failed to load resource/.test(m.text())) return;
    (isLocal(where) || !where ? fail : warn)(`console error: ${m.text().slice(0, 160)}`);
  });
  page.on('response', (r) => {
    const s = r.status();
    if (s < 400) return;
    if (isLocal(r.url())) fail(`${s} ${r.url().replace(ORIGIN, '')}`);
    else if (s === 404 || s === 410) fail(`${s} external ${r.url()}`);
    else warn(`${s} external ${r.url()}`);
  });
  page.on('requestfailed', (r) => {
    const err = r.failure()?.errorText || '';
    if (err.includes('ERR_ABORTED')) return; // e.g. a video fetching only its metadata
    (isLocal(r.url()) ? fail : warn)(`request failed (${err}) ${r.url()}`);
  });

  try {
    const res = await page.goto(ORIGIN + pagePath, { waitUntil: 'networkidle', timeout: 60000 });
    if (pagePath !== '/404.html' && res && res.status() >= 400) fail(`page returned ${res.status()}`);
    await page.waitForTimeout(500); // let late scripts run
    const hrefs = await page.$$eval('a[href]', (as) => as.map((a) => a.href));
    for (const href of hrefs) {
      if (!isLocal(href)) continue;
      const target = new URL(href).pathname;
      if (!linkTargets.has(target)) linkTargets.set(target, pagePath);
    }
  } catch (e) {
    fail(`could not load: ${e.message.split('\n')[0]}`);
  }
  await context.close();
  console.log(`checked ${pagePath}`);
}

for (const [target, from] of linkTargets) {
  if (!resolveFile(target)) failures.push(`${from}: broken link to ${target}`);
}

await browser.close();
server.close();

console.log(`\n${pages.length} pages, ${linkTargets.size} internal link targets checked.`);
if (warnings.length) console.log(`\nWarnings (not failing the build):\n  ${[...new Set(warnings)].join('\n  ')}`);
if (failures.length) {
  console.log(`\nFAILED:\n  ${[...new Set(failures)].join('\n  ')}`);
  process.exit(1);
}
console.log('\nAll pages passed.');
