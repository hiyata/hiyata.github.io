---
layout: default
title: Welcome
---

<!-- External CSS and JS Files -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" />
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">

<script src="{{ '/assets/js/custom.js' | relative_url }}"></script>

<div id="loading-overlay">
  <div class="spinner"></div>
</div>

<div id="content" style="display: none;">
  <!-- Centerpiece Section -->
  <div class="centerpiece-section" id="home">
    <div class="centerpiece-content">
      <div class="pdb-wrapper">
        <div id="pdb-container"></div>
      </div>
      <h1 class="main-title">Hiyata's Technical Journal</h1>
      <div id="typing-container" class="typing-effect"></div>
    </div>
    <div class="scroll-indicator">
      <i class="fas fa-chevron-down"></i>
    </div>
  </div>

  <!-- About Section -->
  <section class="about-section" id="about">
    <div class="container">
      <h2>Exploring the Intersection of AI and Virology</h2>
      <p>Welcome to my technical journal, where I write about my latest projects and ideas. My interests lie at the intersection of AI and virology. I currently work at Wayne State University School of Medicine under <a href="https://www.med.wayne.edu/profile/dx0934">Dr. Phil Pellett</a>. Here, I share my research, the lessons I've learned, and the challenges I've encountered along the way.</p>
      <div class="expertise-areas">
        <div class="expertise-item">
          <i class="fas fa-brain"></i>
          <h3>Machine Learning</h3>
          <p>Advanced machine learning algorithms to learn latent patterns in viral DNA and behavior.</p>
        </div>
        <div class="expertise-item">
          <i class="fas fa-dna"></i>
          <h3>Viral Genomics</h3>
          <p>Using neural networks to for generative genome design and analysis.</p>
        </div>
        <div class="expertise-item">
          <i class="fas fa-virus"></i>
          <h3>Epidemiology</h3>
          <p>Analyzing the spread of viral diseases during outbreaks.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Projects Section -->
  <section class="projects-section" id="projects">
    <div class="container">
      <h2>Recent Projects</h2>
      <div class="projects-list">
        {% for project in site.projects limit:3 %}
          <div class="project-item">
            <h3><a href="{{ project.url | relative_url }}">{{ project.title }}</a></h3>
            <p>{{ project.excerpt | strip_html | truncatewords: 30 }}</p>
            {% if project.presented_at %}
            <span class="presented-at">{{ project.presented_at }}</span>
            {% endif %}
          </div>
        {% endfor %}
      </div>
      <div class="contact-buttons">
      <a href="{{ '/projects' | relative_url }}" class="btn">Explore All Projects</a>
      </div>
    </div>
  </section>

  <!-- Blog Section -->
  <section class="blog-section" id="blog">
    <div class="container">
      <h2>Latest Insights</h2>
      <div class="blog-list">
        {% for post in site.posts limit:2 %}
          <div class="blog-item">
            <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
            <p>{{ post.excerpt | strip_html | truncatewords: 30 }}</p>
            <span class="post-date">{{ post.date | date_to_string }}</span>
          </div>
        {% endfor %}
      </div> 
      <div class="contact-buttons">
      <a href="{{ '/blog' | relative_url }}" class="btn">Read More Insights</a>
      </div>
    </div>
  </section>

  <!-- Contact Section -->
  <section class="contact-section" id="contact">
    <div class="container">
      <h2>Let's Connect</h2>
      <p>Interested in collaborating or have questions about my research? Feel free to reach out!</p>
      <div class="contact-buttons">
        <a href="mailto:ga5808@wayne.edu" class="btn">Email Me</a>
        <a href="linkedin.com/in/alan-luis-carbajo-jr-9929b7138" class="btn">Connect on LinkedIn</a>
      </div>
    </div>
  </section>
</div>

<!-- Styles -->
<style>
  :root {
    --primary-color: #004dff;
    --secondary-color: #00a2ff;
    --accent-color: #ff4d4d;
    --text-color: #2c2c2c;
    --background-color: #ffffff;
    --section-padding: 40px 0;
    --font-family: 'Roboto', sans-serif;
    --max-width: 1100px;
  }

  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }

  body {
    font-family: var(--font-family);
    line-height: 1.6;
    color: var(--text-color);
    background-color: var(--background-color);
    visibility: hidden;
    opacity: 0;
    transition: opacity 0.3s ease-in-out;
  }

  #loading-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: var(--background-color);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 9999;
  }

  .spinner {
    width: 40px;
    height: 40px;
    border: 3px solid var(--primary-color);
    border-top: 3px solid var(--secondary-color);
    border-radius: 50%;
    animation: spin 1s linear infinite;
  }

  @keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
  }

  .container {
    max-width: var(--max-width);
    margin: 0 auto;
    padding: 0 20px;
  }

  h1, h2, h3 {
    font-weight: 700;
    margin-bottom: 20px;
  }

  .centerpiece-section {
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    background-color: var(--background-color);
    padding: 0;
    position: relative;
    flex-direction: column;
  }

  .centerpiece-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    position: relative;
    z-index: 1;
  }

  .pdb-wrapper {
    width: 500px;
    height: 500px;
    margin-bottom: 20px;
    position: relative;
  }

  #pdb-container {
    width: 100%;
    height: 100%;
    position: absolute;
    top: 0;
    left: 0;
  }

  .main-title {
    font-size: 2.8em;
    letter-spacing: 1px;
    margin-bottom: 10px;
    color: var(--primary-color);
  }

  #typing-container {
    font-size: 1.4em;
    height: 1.5em;
    font-weight: 400;
    color: var(--text-color);
  }

  .scroll-indicator {
    position: absolute;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    font-size: 2em;
    color: var(--primary-color);
    animation: bounce 1.5s infinite;
  }

  @keyframes bounce {
    0%, 20%, 50%, 80%, 100% { transform: translateX(-50%) translateY(0); }
    40% { transform: translateX(-50%) translateY(-15px); }
    60% { transform: translateX(-50%) translateY(-7px); }
  }

  section {
    padding: var(--section-padding);
  }

  .about-section {
    background-color: var(--background-color);
    text-align: center;
    padding-top: 0;
  }

  .expertise-areas {
    display: flex;
    justify-content: space-between;
    gap: 20px;
    margin-top: 30px;
  }

  .expertise-item {
    text-align: center;
    max-width: 300px;
  }

  .expertise-item i {
    font-size: 2.2em;
    color: var(--accent-color);
    margin-bottom: 10px;
  }

  .expertise-item h3 {
    color: var(--primary-color);
    font-size: 1.4em;
    margin-bottom: 8px;
  }

  .projects-section, .blog-section {
    background-color: var(--background-color);
    text-align: center;
  }

  .projects-list, .blog-list {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
    margin-top: 30px;
  }

  .project-item, .blog-item {
    background-color: var(--background-color);
    padding: 15px;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
  }

  .project-item:hover, .blog-item:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 20px rgba(0,0,0,0.15);
  }

  .btn {
    display: inline-block;
    padding: 10px 20px;
    background-color: var(--primary-color);
    color: white;
    text-decoration: none;
    border-radius: 5px;
    transition: background-color 0.3s ease, transform 0.3s ease;
    font-weight: 500;
    margin-top: 20px;
    letter-spacing: 0.5px;
  }

  .btn:hover {
    background-color: var(--accent-color);
    transform: translateY(-2px);
  }

  .contact-buttons {
    display: flex;
    justify-content: center;
    gap: 15px;
    margin-top: 20px;
  }

  @media (max-width: 768px) {
    .main-title {
      font-size: 2.2em;
    }

    #typing-container {
      font-size: 1.1em;
    }

    .pdb-wrapper {
      width: 300px;
      height: 300px;
    }

    .expertise-areas {
      flex-direction: column;
      gap: 20px;
    }

    .projects-list, .blog-list {
      grid-template-columns: 1fr;
    }

    .btn {
      width: 100%;
      text-align: center;
    }
  }

  /* Navigation bar visibility on mouse movement */
  #nav {
    position: fixed;
    width: 100%;
    top: 0;
    left: 0;
    background: rgba(255, 255, 255, 0.9);
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    z-index: 1000;
    transform: translateY(-100%);
    transition: transform 0.3s ease-in-out;
  }

  body.show-nav #nav {
    transform: translateY(0);
  }

</style>

<!-- Scripts -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
<script src="https://3Dmol.csb.pitt.edu/build/3Dmol-min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.9.1/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.9.1/ScrollTrigger.min.js"></script>

<script>
  // Ensure the page is hidden until fully loaded
  document.body.style.visibility = 'hidden';
  document.body.style.opacity = '0';

  window.addEventListener('load', function() {
    // Hide loading overlay
    document.getElementById('loading-overlay').style.display = 'none';

    // Show content
    document.getElementById('content').style.display = 'block';

    // Make body visible
    document.body.style.visibility = 'visible';
    document.body.style.opacity = '1';

    // Typing animation
    const typingContainer = document.getElementById('typing-container');
    const texts = [
      "Designing genomes with artificial intelligence",
      "Applying machine learning models to virus predictions",
      "Simulating evolutionary changes in artificial life"
    ];
    let textIndex = 0;
    let charIndex = 0;

    function type() {
      if (charIndex < texts[textIndex].length) {
        typingContainer.innerHTML += texts[textIndex].charAt(charIndex);
        charIndex++;
        setTimeout(type, 100);
      } else {
        setTimeout(erase, 2000);
      }
    }

    function erase() {
      if (charIndex > 0) {
        typingContainer.innerHTML = texts[textIndex].substring(0, charIndex - 1);
        charIndex--;
        setTimeout(erase, 50);
      } else {
        textIndex = (textIndex + 1) % texts.length;
        setTimeout(type, 1000);
      }
    }

    setTimeout(type, 1000);

    // PDB Viewer (Non-interactive, Rotating Ribbon Model)
    let element = $('#pdb-container');
    let config = { backgroundColor: 'white', spin: true, spinSpeed: 1 };
    let viewer = $3Dmol.createViewer(element, config);

    $.get('assets/pdb_files/artificial_hepB_ORF1.pdb', function(data) {
      viewer.addModel(data, "pdb");
      viewer.setStyle({}, { cartoon: { color: 'spectrum' } });
      viewer.zoomTo();
      viewer.render();
      viewer.spin(true);
    });

    // Smooth scrolling
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
          behavior: 'smooth'
        });
      });
    });

    // GSAP Animations
    gsap.registerPlugin(ScrollTrigger);

    gsap.from('.main-title', {
      duration: 1,
      y: 50,
      opacity: 0,
      ease: 'power3.out'
    });

    gsap.from('.expertise-item', {
      scrollTrigger: {
        trigger: '.expertise-areas',
        start: 'top 80%'
      },
      duration: 0.8,
      y: 50,
      opacity: 0,
      stagger: 0.2,
      ease: 'power3.out'
    });

    gsap.from('.project-item, .blog-item', {
      scrollTrigger: {
        trigger: '.projects-section',
        start: 'top 80%'
      },
      duration: 0.8,
      y: 50,
      opacity: 0,
      stagger: 0.2,
      ease: 'power3.out'
    });
  });

  // Show navigation bar only when cursor moves up
  let lastScrollTop = 0;
  const nav = document.getElementById('nav');
  document.addEventListener('mousemove', function(e) {
    if (e.clientY < 100) {
      document.body.classList.add('show-nav');
    } else {
      document.body.classList.remove('show-nav');
    }
  });

  window.addEventListener('scroll', function() {
    let st = window.pageYOffset || document.documentElement.scrollTop;
    if (st > lastScrollTop) {
      // Downscroll
      document.body.classList.remove('show-nav');
    } else {
      // Upscroll
      document.body.classList.add('show-nav');
    }
    lastScrollTop = st <= 0 ? 0 : st;
  }, false);
</script>
