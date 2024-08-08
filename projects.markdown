---
layout: default
title: Projects
permalink: /projects/
---

<div class="projects-container">
  <h1 class="projects-title">My Research Projects</h1>
  
  <div class="project-filter">
    <button class="filter-btn active" data-filter="all">All</button>
    <button class="filter-btn" data-filter="ai">AI & ML</button>
    <button class="filter-btn" data-filter="virology">Virology</button>
    <button class="filter-btn" data-filter="genomics">Genomics</button>
  </div>

  <div class="projects-grid">
    {% for project in site.projects %}
      <div class="project-card" data-category="{{ project.category }}">
        <div class="project-content">
          <h2 class="project-title">{{ project.title }}</h2>
          <p class="project-excerpt">{{ project.excerpt | strip_html | truncate: 100 }}</p>
          <a href="{{ project.url | relative_url }}" class="read-more">Read More</a>
        </div>
        <div class="project-image" style="background-image: url('{{ project.image | relative_url }}')"></div>
      </div>
    {% endfor %}
  </div>
</div>

<div class="dna-animation">
  <svg width="100%" height="200" viewBox="0 0 1000 200">
    <path id="dna-path" d="M0,100 Q250,0 500,100 T1000,100" fill="none" stroke="#3498db" stroke-width="2"/>
    <g id="dna-group"></g>
  </svg>
</div>

<style>
  .projects-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 2rem;
  }

  .projects-title {
    text-align: center;
    font-size: 2.5rem;
    margin-bottom: 2rem;
    color: #2c3e50;
  }

  .project-filter {
    display: flex;
    justify-content: center;
    margin-bottom: 2rem;
  }

  .filter-btn {
    background-color: #ecf0f1;
    border: none;
    padding: 0.5rem 1rem;
    margin: 0 0.5rem;
    cursor: pointer;
    transition: background-color 0.3s ease;
    border-radius: 20px;
  }

  .filter-btn.active, .filter-btn:hover {
    background-color: #3498db;
    color: white;
  }

  .projects-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
  }

  .project-card {
    background-color: white;
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    position: relative;
  }

  .project-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
  }

  .project-content {
    padding: 1.5rem;
  }

  .project-title {
    font-size: 1.5rem;
    margin-bottom: 1rem;
    color: #2c3e50;
  }

  .project-excerpt {
    font-size: 0.9rem;
    color: #7f8c8d;
    margin-bottom: 1rem;
  }

  .read-more {
    display: inline-block;
    padding: 0.5rem 1rem;
    background-color: #3498db;
    color: white;
    text-decoration: none;
    border-radius: 20px;
    transition: background-color 0.3s ease;
  }

  .read-more:hover {
    background-color: #2980b9;
  }

  .project-image {
    height: 200px;
    background-size: cover;
    background-position: center;
  }

  .dna-animation {
    margin-top: 3rem;
  }
</style>

<script src="https://cdnjs.cloudflare.com/ajax/libs/animejs/3.2.1/anime.min.js"></script>
<script>
  document.addEventListener('DOMContentLoaded', () => {
    // Filter functionality
    const filterButtons = document.querySelectorAll('.filter-btn');
    const projectCards = document.querySelectorAll('.project-card');

    filterButtons.forEach(button => {
      button.addEventListener('click', () => {
        const filter = button.dataset.filter;
        
        filterButtons.forEach(btn => btn.classList.remove('active'));
        button.classList.add('active');

        projectCards.forEach(card => {
          if (filter === 'all' || card.dataset.category === filter) {
            card.style.display = 'block';
          } else {
            card.style.display = 'none';
          }
        });
      });
    });

    // DNA Animation
    const dnaGroup = document.getElementById('dna-group');
    const dnaPath = document.getElementById('dna-path');
    const pathLength = dnaPath.getTotalLength();

    for (let i = 0; i < 20; i++) {
      const circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
      circle.setAttribute('r', '4');
      circle.setAttribute('fill', i % 2 === 0 ? '#e74c3c' : '#2ecc71');
      dnaGroup.appendChild(circle);
    }

    anime({
      targets: '#dna-group circle',
      translateX: (el, i) => {
        const progress = (i / 19) * pathLength;
        const point = dnaPath.getPointAtLength(progress);
        return point.x;
      },
      translateY: (el, i) => {
        const progress = (i / 19) * pathLength;
        const point = dnaPath.getPointAtLength(progress);
        return point.y;
      },
      scale: (el, i) => anime.random(0.5, 1),
      easing: 'easeInOutSine',
      duration: 4000,
      loop: true,
      direction: 'alternate',
      delay: (el, i) => i * 100,
    });

    // Project card animation
    anime({
      targets: '.project-card',
      opacity: [0, 1],
      translateY: [50, 0],
      easing: 'easeOutExpo',
      duration: 1000,
      delay: anime.stagger(200),
    });
  });
</script>