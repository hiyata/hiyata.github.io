// stream-transition.js
document.addEventListener('DOMContentLoaded', () => {
    const overlay = document.querySelector('.page-transition-overlay');
    const body = document.body;

    // Function to show the overlay
    function showOverlay() {
        overlay.classList.add('active');
    }

    // Function to hide the overlay
    function hideOverlay() {
        overlay.classList.remove('active');
        body.classList.add('loaded');
    }

    // Show overlay immediately when the script runs
    showOverlay();

    // Hide overlay after a delay (simulating page load)
    setTimeout(hideOverlay, 1500);

    // Add event listener for all internal links
    document.querySelectorAll('a').forEach(link => {
        if (link.host === window.location.host) {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                showOverlay();
                setTimeout(() => {
                    window.location = link.href;
                }, 500);
            });
        }
    });
});