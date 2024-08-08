---
layout: default
title: About
permalink: /about/
---

<div class="about-container">
  <div class="profile-section">
    <div class="profile-image-container">
      <div class="profile-image"></div>
    </div>
    <h1 class="name">Hiyata</h1>
    <p class="title">Machine Learning Researcher in Virology</p>
  </div>

  <div class="about-content">
    <h2>About Me</h2>
    <p>I am a researcher specializing in the intersection of machine learning and virology. My work primarily focuses on developing computational techniques to model virus behavior and their molecular interactions.</p>
    
    <p>By applying machine learning algorithms to vast datasets of viral genomes and epidemiological information, I aim to uncover patterns and insights that can lead to better predictive models and innovative solutions in virology.</p>

    <div class="skills-container">
      <h3>Core Competencies</h3>
      <ul class="skills-list">
        <li class="skill-item" data-skill="Machine Learning">Machine Learning</li>
        <li class="skill-item" data-skill="Deep Learning">Deep Learning</li>
        <li class="skill-item" data-skill="Virology">Virology</li>
        <li class="skill-item" data-skill="Genomics">Genomics</li>
        <li class="skill-item" data-skill="Data Analysis">Data Analysis</li>
        <li class="skill-item" data-skill="Bioinformatics">Bioinformatics</li>
      </ul>
    </div>

    <div class="research-focus">
      <h3>Research Focus</h3>
      <div class="focus-items">
        <div class="focus-item">
          <div class="focus-icon">🧬</div>
          <p>Viral Genome Analysis</p>
        </div>
        <div class="focus-item">
          <div class="focus-icon">🦠</div>
          <p>Epidemiological Modeling</p>
        </div>
        <div class="focus-item">
          <div class="focus-icon">🧪</div>
          <p>Drug Discovery</p>
        </div>
        <div class="focus-item">
          <div class="focus-icon">🔬</div>
          <p>Virus-Host Interactions</p>
        </div>
      </div>
    </div>

    <div class="publications">
      <h3>Recent Publications</h3>
      <ul class="publication-list">
        <li>
          <span class="pub-title">"Machine Learning Approaches in Viral Genomics"</span>
          <span class="pub-journal">Cool fun Journal</span>
        </li>
        <li>
          <span class="pub-title">"Predicting Viral Mutations Using Deep Learning Models"</span>
          <span class="pub-journal">Journal of really cool things</span>
        </li>
        <li>
          <span class="pub-title">"AI-Driven Strategies for Antiviral Drug Discovery"</span>
          <span class="pub-journal">Journal of robots and viruses</span>
        </li>
      </ul>
    </div>
  </div>
</div>

<div class="dna-animation">
  <svg id="dna-svg" width="100%" height="200" viewBox="0 0 1000 200"></svg>
</div>

<style>
  .about-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 40px 20px;
    font-family: 'Arial', sans-serif;
    color: #333;
  }

  .profile-section {
    text-align: center;
    margin-bottom: 40px;
  }

  .profile-image-container {
    width: 200px;
    height: 200px;
    margin: 0 auto 20px;
    border-radius: 50%;
    overflow: hidden;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
  }

  .profile-image {
    width: 100%;
    height: 100%;
    background-image: url('path_to_your_image.jpg');
    background-size: cover;
    background-position: center;
  }

  .name {
    font-size: 2.5em;
    margin-bottom: 10px;
    color: #2c3e50;
  }

  .title {
    font-size: 1.2em;
    color: #7f8c8d;
  }

  .about-content {
    line-height: 1.6;
  }

  h2, h3 {
    color: #2c3e50;
    margin-top: 30px;
  }

  .skills-container {
    margin-top: 30px;
  }

  .skills-list {
    list-style-type: none;
    padding: 0;
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
  }

  .skill-item {
    background-color: #3498db;
    color: white;
    padding: 8px 15px;
    border-radius: 20px;
    font-size: 0.9em;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
  }

  .skill-item:hover {
    transform: translateY(-3px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }

  .research-focus {
    margin-top: 30px;
  }

  .focus-items {
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 20px;
  }

  .focus-item {
    text-align: center;
    flex-basis: calc(50% - 10px);
  }

  .focus-icon {
    font-size: 2.5em;
    margin-bottom: 10px;
  }

  .publications {
    margin-top: 30px;
  }

  .publication-list {
    list-style-type: none;
    padding: 0;
  }

  .publication-list li {
    margin-bottom: 15px;
  }

  .pub-title {
    font-weight: bold;
    display: block;
  }

  .pub-journal {
    font-style: italic;
    color: #7f8c8d;
  }

  .dna-animation {
    margin-top: 50px;
  }
</style>

<script src="https://cdnjs.cloudflare.com/ajax/libs/animejs/3.2.1/anime.min.js"></script>
<script>
  // DNA Animation
  const svg = document.getElementById('dna-svg');
  const width = 1000;
  const height = 200;
  const numBases = 20;
  const baseWidth = width / numBases;
  const helixOffset = 40; // Vertical offset for the helix twist

  for (let i = 0; i < numBases; i++) {
    const x = i * baseWidth + baseWidth / 2;
    // Double helix calculation with sinusoidal offset
    const y1 = height / 2 + helixOffset * Math.sin(i * 2 * Math.PI / numBases + Math.PI); // Second helical path
    const y2 = height / 2 + helixOffset * Math.sin(i * 2 * Math.PI / numBases);

    // Create circles for base pairs
    const circle1 = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
    circle1.setAttribute('cx', x);
    circle1.setAttribute('cy', y1);
    circle1.setAttribute('r', '5');
    circle1.setAttribute('fill', '#e74c3c');
    svg.appendChild(circle1);

    const circle2 = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
    circle2.setAttribute('cx', x);
    circle2.setAttribute('cy', y2);
    circle2.setAttribute('r', '5');
    circle2.setAttribute('fill', '#2ecc71');
    svg.appendChild(circle2);
  }

  // Continuous animation with forward and backward movement
  anime({
    targets: '#dna-svg circle:nth-child(odd)',
    translateY: function(el) {
      return parseFloat(el.nextElementSibling.getAttribute('cy')) - parseFloat(el.getAttribute('cy'));
    },
    duration: 1000,
    loop: true,
    easing: 'linear',
    delay: function(el, i) {
      return i * 100;
    },
    direction: 'alternate' // Movement forward then reverse
  });

  anime({
    targets: '#dna-svg circle:nth-child(even)',
    translateY: function(el) {
      return parseFloat(el.previousElementSibling.getAttribute('cy')) - parseFloat(el.getAttribute('cy'));
    },
    duration: 1000,
    loop: true,
    easing: 'linear',
    delay: function(el, i) {
      return 50 + i * 100;
    },
    direction: 'alternate' // Movement forward then reverse
  });
</script>
