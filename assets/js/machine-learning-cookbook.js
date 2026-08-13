document.addEventListener('DOMContentLoaded', function () {
  const article = document.querySelector('.cookbook-content');
  if (!article) return;

  /* ---------------- Reading progress bar ---------------- */
  const progressBar = document.getElementById('cookbook-progress');
  if (progressBar) {
    const updateProgress = () => {
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      const pct = docHeight > 0 ? (window.scrollY / docHeight) * 100 : 0;
      progressBar.style.width = Math.min(100, Math.max(0, pct)) + '%';
    };
    window.addEventListener('scroll', updateProgress, { passive: true });
    window.addEventListener('resize', updateProgress);
    updateProgress();
  }

  /* ---------------- Auto-generated TOC + scroll spy ---------------- */
  const tocList = document.getElementById('toc-list');
  const headings = article.querySelectorAll('h2, h3');

  if (tocList && headings.length) {
    const links = [];
    headings.forEach((heading, i) => {
      if (!heading.id) heading.id = 'section-' + i;
      const link = document.createElement('a');
      link.href = '#' + heading.id;
      link.textContent = heading.textContent;
      link.className = heading.tagName === 'H2' ? 'toc-h2' : 'toc-h3';
      tocList.appendChild(link);
      links.push({ heading, link });
    });

    if ('IntersectionObserver' in window) {
      const observer = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            const match = links.find((l) => l.heading === entry.target);
            if (!match) return;
            if (entry.isIntersecting) {
              links.forEach((l) => l.link.classList.remove('active'));
              match.link.classList.add('active');
            }
          });
        },
        { rootMargin: '-15% 0px -70% 0px', threshold: 0 }
      );
      headings.forEach((h) => observer.observe(h));
    }
  }

  /* ---------------- Wrap tables for horizontal scroll on small screens ---------------- */
  article.querySelectorAll('table').forEach((table) => {
    const wrapper = document.createElement('div');
    wrapper.className = 'table-scroll';
    table.parentNode.insertBefore(wrapper, table);
    wrapper.appendChild(table);
  });

  /* ---------------- Model architecture table search ---------------- */
  const searchInput = document.getElementById('model-arch-search');
  const searchCount = document.getElementById('model-arch-count');
  const archTable = document.getElementById('model-arch-table');

  if (searchInput && archTable) {
    const rows = Array.from(archTable.querySelectorAll('tbody tr'));
    const total = rows.length;

    const updateCount = (shown) => {
      if (searchCount) searchCount.textContent = shown + ' of ' + total + ' shown';
    };
    updateCount(total);

    searchInput.addEventListener('input', () => {
      const query = searchInput.value.trim().toLowerCase();
      let shown = 0;
      rows.forEach((row) => {
        const matches = !query || row.textContent.toLowerCase().includes(query);
        row.style.display = matches ? '' : 'none';
        if (matches) shown += 1;
      });
      updateCount(shown);
    });
  }
});
