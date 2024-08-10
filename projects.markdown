---
layout: default
title: Research Projects
permalink: /projects/
---

<div class="projects-container">
  <h1 class="projects-title">Exploring the Frontiers of AI and Virology</h1>
  
  <div class="project-filter">
    <button class="filter-btn active" data-filter="all">All Projects</button>
    <button class="filter-btn" data-filter="ai">AI & Machine Learning</button>
    <button class="filter-btn" data-filter="virology">Virology</button>
    <button class="filter-btn" data-filter="genomics">Genomics</button>
  </div>

  <div class="projects-grid">
    {% for project in site.projects %}
      <div class="project-card" data-category="{{ project.category }}">
        <div class="project-category">{{ project.category | capitalize }}</div>
        <h2 class="project-title">{{ project.title }}</h2>
        <p class="project-excerpt">{{ project.excerpt | strip_html | truncate: 100 }}</p>
        <a href="{{ project.url | relative_url }}" class="read-more">Explore Project</a>
      </div>
    {% endfor %}
  </div>
</div>

<style>
  .projects-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 2rem;
    background-color: #f9f9f9;
  }

  .projects-title {
    text-align: center;
    font-size: 2rem;
    margin-bottom: 1.5rem;
    color: #2c3e50;
  }

  .project-filter {
    display: flex;
    justify-content: center;
    margin-bottom: 1.5rem;
    flex-wrap: wrap;
  }

  .filter-btn {
    background-color: #ecf0f1;
    border: none;
    padding: 0.5rem 1rem;
    margin: 0.25rem;
    cursor: pointer;
    transition: all 0.3s ease;
    border-radius: 20px;
    font-weight: bold;
    color: #34495e;
  }

  .filter-btn.active, .filter-btn:hover {
    background-color: #3498db;
    color: white;
  }

  .projects-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 1rem;
  }

  .project-card {
    background-color: white;
    border-radius: 8px;
    padding: 1rem;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease;
    display: flex;
    flex-direction: column;
  }

  .project-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
  }

  .project-category {
    align-self: flex-start;
    background-color: #3498db;
    color: white;
    padding: 0.25rem 0.5rem;
    border-radius: 12px;
    font-size: 0.75rem;
    margin-bottom: 0.5rem;
  }

  .project-title {
    font-size: 1.25rem;
    margin-bottom: 0.5rem;
    color: #2c3e50;
  }

  .project-excerpt {
    font-size: 0.9rem;
    color: #7f8c8d;
    margin-bottom: 1rem;
    flex-grow: 1;
  }

  .read-more {
    display: inline-block;
    padding: 0.5rem 1rem;
    background-color: #3498db;
    color: white;
    text-decoration: none;
    border-radius: 20px;
    transition: all 0.3s ease;
    font-weight: bold;
    text-align: center;
    font-size: 0.9rem;
  }

  .read-more:hover {
    background-color: #2980b9;
  }

  @media (max-width: 768px) {
    .projects-grid {
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    }
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
            card.style.display = 'flex';
          } else {
            card.style.display = 'none';
          }
        });

        // Animate the filtered cards
        anime({
          targets: '.project-card[style="display: flex"]',
          opacity: [0, 1],
          translateY: [20, 0],
          easing: 'easeOutExpo',
          duration: 600,
          delay: anime.stagger(100),
        });
      });
    });

    // Initial animation for project cards
    anime({
      targets: '.project-card',
      opacity: [0, 1],
      translateY: [20, 0],
      easing: 'easeOutExpo',
      duration: 800,
      delay: anime.stagger(100),
    });
  });
</script>