---
layout: default
title: Welcome
---

<script src="{{ '/assets/js/custom.js' | relative_url }}"></script>
<div id="loading-overlay">
  <div class="spinner"></div>
</div>

<div id="content" style="display: none;">
  <div class="hero-section" id="home">
    <div class="hero-content">
      <h1 class="main-title">Hiyata's Technical Journal</h1>
      <div id="typing-container"></div>
    </div>
    <div class="scroll-indicator">
      <div class="mouse"></div>
    </div>
  </div>

  <section class="about-section" id="about">
    <div class="container">
      <h2>Exploring the Intersection of AI and Virology</h2>
      <p>Thanks for visiting my page! Here I talk about my current projects and new ideas. I also write about the problems and things I've learned in research. My research interests lie in the intersection of artificial intelligence and virology. I am specifically focused on epidemiology, artificial genome design, artificial life, and virus-host networks.</p>
      <div class="expertise-areas">
        <div class="expertise-item">
          <h3>Machine Learning</h3>
          <p>Applying advanced algorithms to uncover patterns in viral data.</p>
        </div>
        <div class="expertise-item">
          <h3>Viral Genomics</h3>
          <p>Decoding the genetic blueprint of viruses to understand their behavior.</p>
        </div>
        <div class="expertise-item">
          <h3>Epidemiology</h3>
          <p>Studying the spread and control of viral diseases in populations.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="visualization-section" id="visualization">
    <div class="container">
      <h2>Visualizing Viral Structures</h2>
      <div class="pdb-wrapper">
        <div id="pdb-container"></div>
      </div>
      <p class="pdb-caption">Artificial Hepatitis B DNA Polymerase</p>
    </div>
  </section>

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
      <a href="{{ '/projects' | relative_url }}" class="btn">Explore All Projects</a>
    </div>
  </section>

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
      <a href="{{ '/blog' | relative_url }}" class="btn">Read More Insights</a>
    </div>
  </section>

  <section class="contact-section" id="contact">
    <div class="container">
      <h2>Let's Connect</h2>
      <p>Interested in collaboration or have questions about my research? I'd love to hear from you!</p>
      <div class="contact-buttons">
        <a href="mailto:ga5808@wayne.edu" class="btn">Email Me</a>
        <a href="https://www.linkedin.com/in/yourprofile" class="btn">Connect on LinkedIn</a>
      </div>
    </div>
  </section>
</div>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

  :root {
    --primary-color: #0078d7;
    --secondary-color: #00a2ff;
    --text-color: #333;
    --background-color: #f9f9f9;
    --section-padding: 80px 0;
  }

  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }

  body {
    font-family: 'Poppins', sans-serif;
    line-height: 1.6;
    color: var(--text-color);
    background-color: var(--background-color);
    visibility: hidden;
    opacity: 0;
    transition: opacity 0.3s ease;
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
    width: 50px;
    height: 50px;
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
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
  }

  h1, h2, h3 {
    margin-bottom: 20px;
  }

  .hero-section {
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
    color: white;
  }

  .hero-content {
    max-width: 800px;
  }

  .main-title {
    font-size: 3.5em;
    font-weight: 700;
    margin-bottom: 20px;
  }

  #typing-container {
    font-size: 1.8em;
    height: 1.5em;
    font-weight: 300;
  }

  .scroll-indicator {
    position: absolute;
    bottom: 30px;
    left: 50%;
    transform: translateX(-50%);
  }

  .mouse {
    width: 30px;
    height: 50px;
    border: 2px solid white;
    border-radius: 20px;
    position: relative;
  }

  .mouse::before {
    content: '';
    position: absolute;
    top: 10px;
    left: 50%;
    transform: translateX(-50%);
    width: 6px;
    height: 6px;
    background-color: white;
    border-radius: 50%;
    animation: scroll 1.5s infinite;
  }

  @keyframes scroll {
    0% { transform: translate(-50%, 0); opacity: 0; }
    40% { opacity: 1; }
    80% { transform: translate(-50%, 20px); opacity: 0; }
    100% { opacity: 0; }
  }

  section {
    padding: var(--section-padding);
  }

  .about-section, .projects-section, .blog-section {
    background-color: white;
  }

  .visualization-section, .contact-section {
    background-color: var(--background-color);
  }

  .expertise-areas {
    display: flex;
    justify-content: space-between;
    gap: 30px;
    margin-top: 40px;
  }

  .expertise-item {
    flex: 1;
  }

  .expertise-item h3 {
    color: var(--primary-color);
  }

  .pdb-wrapper {
    width: 100%;
    height: 500px;
    margin: 40px 0;
    position: relative;
  }

  #pdb-container {
    width: 100%;
    height: 100%;
    position: absolute;
    top: 0;
    left: 0;
  }

  .pdb-caption {
    text-align: center;
    font-style: italic;
    margin-top: 20px;
  }

  .projects-list, .blog-list {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 30px;
    margin-top: 40px;
  }

  .project-item, .blog-item {
    background-color: var(--background-color);
    padding: 20px;
    border-radius: 8px;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
  }

  .project-item:hover, .blog-item:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 20px rgba(0,0,0,0.1);
  }

  .btn {
    display: inline-block;
    padding: 12px 24px;
    background-color: var(--primary-color);
    color: white;
    text-decoration: none;
    border-radius: 5px;
    transition: background-color 0.3s ease, transform 0.3s ease;
    margin-top: 30px;
    font-weight: 600;
  }

  .btn:hover {
    background-color: var(--secondary-color);
    transform: translateY(-2px);
  }

  .contact-buttons {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin-top: 30px;
  }

  /* Mobile Styles */
  @media (max-width: 768px) {
    .main-title {
      font-size: 2.5em;
    }

    #typing-container {
      font-size: 1.4em;
    }

    .expertise-areas {
      flex-direction: column;
    }

    .projects-list, .blog-list {
      grid-template-columns: 1fr;
    }

    .pdb-wrapper {
      height: 300px;
    }

    .contact-buttons {
      flex-direction: column;
      align-items: center;
    }

    .btn {
      width: 100%;
      text-align: center;
    }
  }

  /* Tablet Styles */
  @media (min-width: 769px) and (max-width: 1024px) {
    .projects-list, .blog-list {
      grid-template-columns: repeat(2, 1fr);
    }
  }
</style>

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
    "Designing Genomes with Artificial Intelligence",
    "Applying Machine Learning Models to Virus Predictions",
    "Simulating Life and Evolution"
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

  // PDB Viewer
  let element = $('#pdb-container');
  let config = { backgroundColor: 'transparent' };
  let viewer = $3Dmol.createViewer(element, config);
  
  $.get('assets/pdb_files/artificial_hepB_ORF1.pdb', function(data) {
    viewer.addModel(data, "pdb");
    viewer.setStyle({}, {stick: {colorscheme:'spectral'}});
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
</script>