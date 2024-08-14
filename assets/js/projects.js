document.addEventListener('DOMContentLoaded', () => {
    const filterButtons = document.querySelectorAll('.filter-btn');
    const projectCards = document.querySelectorAll('.project-card');
    const projectsGrid = document.querySelector('.projects-grid');
  
    // Initialize AOS
    AOS.init({
      duration: 1000,
      once: true,
      offset: 100
    });
  
    filterButtons.forEach(button => {
      button.addEventListener('click', () => {
        const filter = button.dataset.filter;
        
        filterButtons.forEach(btn => btn.classList.remove('active'));
        button.classList.add('active');
  
        projectsGrid.style.height = `${projectsGrid.offsetHeight}px`;
  
        projectCards.forEach(card => {
          if (filter === 'all' || card.dataset.category === filter) {
            card.classList.remove('hidden');
            card.style.display = 'block';
            setTimeout(() => {
              card.style.opacity = '1';
              card.style.transform = 'scale(1)';
            }, 10);
          } else {
            card.style.opacity = '0';
            card.style.transform = 'scale(0.8)';
            setTimeout(() => {
              card.style.display = 'none';
              card.classList.add('hidden');
            }, 300);
          }
        });
  
        setTimeout(() => {
          projectsGrid.style.height = 'auto';
        }, 300);
      });
    });
  
    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
          behavior: 'smooth'
        });
      });
    });
  
    // Add hover effect to dim other cards
    projectCards.forEach(card => {
      card.addEventListener('mouseenter', () => {
        projectCards.forEach(otherCard => {
          if (otherCard !== card && !otherCard.classList.contains('hidden')) {
            otherCard.style.opacity = '0.6';
            otherCard.style.transform = 'scale(0.98)';
          }
        });
      });
  
      card.addEventListener('mouseleave', () => {
        projectCards.forEach(otherCard => {
          if (!otherCard.classList.contains('hidden')) {
            otherCard.style.opacity = '1';
            otherCard.style.transform = 'scale(1)';
          }
        });
      });
    });
  
    // Lazy load images
    const lazyImages = document.querySelectorAll('.project-image');
    const lazyImageObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const img = entry.target;
          img.style.backgroundImage = `url(${img.dataset.src})`;
          img.classList.add('loaded');
          lazyImageObserver.unobserve(img);
        }
      });
    });
  
    lazyImages.forEach(image => {
      lazyImageObserver.observe(image);
    });
  });

  document.addEventListener('DOMContentLoaded', () => {
    const filterButtons = document.querySelectorAll('.filter-btn');
    const projectCards = document.querySelectorAll('.project-card');
    const projectsGrid = document.querySelector('.projects-grid');
  
    let currentFilter = 'all';
  
    function updateLayout() {
      const visibleCards = document.querySelectorAll('.project-card:not(.hidden)');
      visibleCards.forEach((card, index) => {
        card.style.gridColumn = `auto / span 1`;
        card.style.gridRow = `auto / span 1`;
      });
    }
  
    function filterProjects(filter) {
      projectCards.forEach(card => {
        if (filter === 'all' || card.dataset.category === filter) {
          card.classList.remove('hidden');
          card.style.opacity = '1';
          card.style.transform = 'scale(1)';
        } else {
          card.classList.add('hidden');
          card.style.opacity = '0';
          card.style.transform = 'scale(0.8)';
        }
      });
  
      setTimeout(updateLayout, 300);
    }
  
    filterButtons.forEach(button => {
      button.addEventListener('click', () => {
        const filter = button.dataset.filter;
        if (filter === currentFilter) return;
  
        filterButtons.forEach(btn => btn.classList.remove('active'));
        button.classList.add('active');
  
        currentFilter = filter;
        filterProjects(filter);
      });
    });
  
    // Initial layout
    updateLayout();
  });