---
layout: default
title: Project Showcase
permalink: /projects/
custom_css: projects
custom_js: projects
---

<header class="projects-header">
  <div class="header-content">
    <h1 class="header-title">Research Projects</h1>
    <p class="header-subtitle">Showcasing the projects myself and our lab has worked on.</p>
  </div>
</header>

<div class="projects-container">
  <div class="project-filter">
    <button class="filter-btn active" data-filter="all">All Projects</button>
    <button class="filter-btn" data-filter="ai">AI & Machine Learning</button>
    <button class="filter-btn" data-filter="virology">Virology</button>
    <button class="filter-btn" data-filter="genomics">Genomics</button>
  </div>

  <div class="projects-grid">
    {% for project in site.projects %}
      <div class="project-card" data-category="{{ project.category }}">
        <div class="project-header">
          <span class="project-category">{{ project.category | capitalize }}</span>
          {% if project.presented_at %}
            <span class="presented-at" title="{{ project.presented_at }}">{{ project.presented_at }}</span>
          {% endif %}
        </div>
        <div class="project-body">
          <h2 class="project-title">{{ project.title }}</h2>
          <p class="project-excerpt">{{ project.excerpt | strip_html | truncate: 120 }}</p>
          <div class="project-meta">
            <span class="project-date">{{ project.date | date: "%B %Y" }}</span>
            <a href="{{ project.url | relative_url }}" class="read-more">View Details</a>
          </div>
        </div>
      </div>
    {% endfor %}
  </div>
</div>

<section class="cta-section">
  <div class="cta-content">
    <h2 class="cta-title">Interested in Collaboration?</h2>
    <p class="cta-text">I'm always open to new research opportunities and partnerships.</p>
    <a href="/contact" class="cta-button">Get in Touch</a>
  </div>
</section>