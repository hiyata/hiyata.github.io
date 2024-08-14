document.addEventListener('DOMContentLoaded', function() {
  const transitionOverlay = document.getElementById('page-transition-overlay');
  const transitionDuration = 500; // ms
  const minimumLoadTime = 200; // ms

  function fadeIn(element) {
    return new Promise((resolve) => {
      element.style.opacity = 0;
      element.style.display = 'block';
      
      (function fade() {
        let val = parseFloat(element.style.opacity);
        if (!((val += .1) > 1)) {
          element.style.opacity = val;
          requestAnimationFrame(fade);
        } else {
          resolve();
        }
      })();
    });
  }

  function startTransition(url) {
    document.body.classList.add('page-transitioning');
    
    const transitionStart = Date.now();
    
    fadeIn(transitionOverlay).then(() => {
      const elapsedTime = Date.now() - transitionStart;
      const remainingTime = Math.max(minimumLoadTime - elapsedTime, 0);
      
      setTimeout(() => {
        window.location.href = url;
      }, remainingTime);
    });
  }
  
  document.body.addEventListener('click', function(e) {
    const anchor = e.target.closest('a');
    if (anchor && anchor.href && anchor.href.startsWith(window.location.origin) && !anchor.getAttribute('target')) {
      e.preventDefault();
      startTransition(anchor.href);
    }
  });
  
  window.addEventListener('pageshow', function(event) {
    if (event.persisted) {
      document.body.classList.remove('page-transitioning');
      transitionOverlay.style.opacity = 0;
      transitionOverlay.style.display = 'none';
    }
  });
  
  window.addEventListener('load', function() {
    document.body.classList.remove('page-transitioning');
    transitionOverlay.style.opacity = 0;
    setTimeout(() => {
      transitionOverlay.style.display = 'none';
    }, transitionDuration);
  });

  // Initial page load transition
  document.body.classList.add('page-transitioning');
  transitionOverlay.style.opacity = 1;
  transitionOverlay.style.display = 'block';
});
