# hiyata.github.io

Source for [hiyata.github.io](https://hiyata.github.io): AI × virology project write-ups,
interactive tools, and USMLE practice banks. Built with Jekyll (minima theme, heavily
customised).

## Run locally

    bundle install
    bundle exec jekyll serve      # http://localhost:4000

## Deploy

Pushing to `main` runs `.github/workflows/deploy.yml`, which builds with the Jekyll
version pinned in `Gemfile.lock` and publishes to GitHub Pages. The same workflow
redeploys after the scheduled feed update (`update-feeds.yml`), so the Reading page
stays current.

## Layout

| Path | What it is |
| --- | --- |
| `_projects/` | Project pages (the `projects` collection, served under `/projects/` unless a page sets its own `permalink`) |
| `_posts/` | Blog posts, listed on `/blog/` |
| `_layouts/`, `_includes/` | Page shells, header and footer |
| `assets/css`, `assets/js` | A page opts into `<name>.css` / `<name>.js` with `custom_css:` / `custom_js:` in its front matter |
| `assets/data/` | PubMed and arXiv feeds, refreshed every 6 hours by `.github/scripts/update_feeds.py` |
| `assets/js/nbme/`, `assets/images/nbme/` | Question banks and images for the NBME-style practice exams |
| `tools/nbme-micro/` | Generator for the microbiology bank and encyclopedia; see its README. Not published. |

Images are WebP.
