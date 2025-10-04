document.addEventListener('DOMContentLoaded', () => {
  const overlay = document.getElementById('loading-overlay');
  const viewport = document.querySelector('.home-viewport');
  const header = document.querySelector('.site-header');
  const navToggle = document.querySelector('.nav-toggle');
  const navLinks = document.querySelectorAll('.nav-link[data-nav-section]');
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const supportsIntersectionObserver = 'IntersectionObserver' in window;

  document.querySelectorAll('[data-animate]').forEach((element) => {
    const delay = element.dataset.animateDelay;
    if (delay) {
      element.style.setProperty('--animate-delay', `${delay}ms`);
    }
  });

  if (supportsIntersectionObserver) {
    const animateObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            animateObserver.unobserve(entry.target);
          }
        });
      },
      {
        threshold: 0.2,
      }
    );

    document.querySelectorAll('[data-animate]').forEach((el) => animateObserver.observe(el));
  } else {
    document.querySelectorAll('[data-animate]').forEach((el) => el.classList.add('is-visible'));
  }

  const navSections = new Map();
  navLinks.forEach((link) => {
    const sectionId = link.dataset.navSection;
    if (!sectionId) return;
    const section = document.getElementById(sectionId);
    if (section) {
      navSections.set(sectionId, { link, section });
    }
  });

  const setActiveNav = (id) => {
    navLinks.forEach((link) => link.classList.remove('is-active'));
    if (id && navSections.has(id)) {
      navSections.get(id).link.classList.add('is-active');
    }
  };

  if (supportsIntersectionObserver && navSections.size) {
    const sectionObserver = new IntersectionObserver(
      (entries) => {
        entries
          .filter((entry) => entry.isIntersecting)
          .sort((a, b) => b.intersectionRatio - a.intersectionRatio)
          .forEach((entry) => setActiveNav(entry.target.id));
      },
      {
        rootMargin: '-45% 0px -45% 0px',
        threshold: [0.25, 0.5, 0.75],
      }
    );

    navSections.forEach(({ section }) => sectionObserver.observe(section));
  } else if (!supportsIntersectionObserver && navSections.size) {
    const firstSection = navSections.keys().next().value;
    setActiveNav(firstSection);
  }

  if (navToggle) {
    navToggle.addEventListener('click', () => {
      const expanded = navToggle.getAttribute('aria-expanded') === 'true';
      navToggle.setAttribute('aria-expanded', String(!expanded));
      header?.classList.toggle('nav-open', !expanded);
    });
  }

  navLinks.forEach((link) => {
    link.addEventListener('click', () => {
      if (header?.classList.contains('nav-open')) {
        header.classList.remove('nav-open');
        navToggle?.setAttribute('aria-expanded', 'false');
      }
    });
  });

  let lastScrollY = window.scrollY;
  let ticking = false;

  const handleScroll = () => {
    const currentY = window.scrollY;
    if (header) {
      header.classList.toggle('is-scrolled', currentY > 16);
      if (currentY > lastScrollY && currentY > 120) {
        header.classList.add('is-hidden');
      } else {
        header.classList.remove('is-hidden');
      }
    }
    lastScrollY = currentY;
    ticking = false;
  };

  window.addEventListener('scroll', () => {
    if (!ticking) {
      window.requestAnimationFrame(handleScroll);
      ticking = true;
    }
  });

  const typingElement = document.querySelector('[data-typing]');
  const typingPhrases = [
    'diffusion models for genome generation',
    'latent viral phenotype prediction',
    'interactive tools for scientific storytelling',
  ];

  if (typingElement && prefersReducedMotion) {
    typingElement.textContent = typingPhrases[0];
  }

  if (typingElement && !prefersReducedMotion) {
    let phraseIndex = 0;
    let characterIndex = 0;
    let typingForward = true;

    const type = () => {
      if (!typingElement) return;

      const currentPhrase = typingPhrases[phraseIndex];
      typingElement.textContent = currentPhrase.substring(0, characterIndex);

      if (typingForward) {
        if (characterIndex < currentPhrase.length) {
          characterIndex += 1;
          setTimeout(type, 80);
        } else {
          typingForward = false;
          setTimeout(type, 1800);
        }
      } else {
        if (characterIndex > 0) {
          characterIndex -= 1;
          setTimeout(type, 45);
        } else {
          typingForward = true;
          phraseIndex = (phraseIndex + 1) % typingPhrases.length;
          setTimeout(type, 500);
        }
      }
    };

    type();
  }

  const initialiseViewer = () => {
    const container = document.getElementById('pdb-container');
    if (!container || typeof window.$3Dmol === 'undefined') {
      return false;
    }

    fetch('assets/pdb_files/artificial_hepB_ORF1.pdb')
      .then((response) => response.text())
      .then((data) => {
        const viewer = window.$3Dmol.createViewer(container, {
          backgroundColor: 'transparent',
        });
        viewer.addModel(data, 'pdb');
        viewer.setStyle({}, { cartoon: { color: 'spectrum' } });
        viewer.zoomTo();
        viewer.render();
        if (!prefersReducedMotion) {
          viewer.spin(true);
        }
      })
      .catch((error) => {
        console.error('Unable to initialise molecular viewer', error);
      });

    return true;
  };

  const tryInitialiseViewer = () => {
    if (initialiseViewer()) {
      return;
    }
    const fallbackTimer = setInterval(() => {
      if (initialiseViewer()) {
        clearInterval(fallbackTimer);
      }
    }, 250);
    setTimeout(() => clearInterval(fallbackTimer), 8000);
  };

  window.addEventListener('load', () => {
    viewport?.classList.add('is-ready');
    overlay?.classList.add('is-hidden');
    setTimeout(() => overlay?.remove(), 600);
    tryInitialiseViewer();
  });
});
