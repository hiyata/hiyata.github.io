---
layout: default
title: Project Showcase
permalink: /projects/
custom_css: projects
custom_js: projects
---

<header class="projects-header">
  <div class="header-content">
    <span class="kicker">Archive</span>
    <h1 class="header-title">Research Projects</h1>
    <p class="header-subtitle">Projects I've worked on, on my own and with the lab.</p>
  </div>
</header>

<div class="projects-container">
  <div class="project-filter">
    <button class="filter-btn active" data-filter="all">All Projects</button>
    <button class="filter-btn" data-filter="ai">AI & Machine Learning</button>
    <button class="filter-btn" data-filter="virology">Virology</button>
    <button class="filter-btn" data-filter="genomics">Genomics</button>
    <button class="filter-btn" data-filter="physiology">Physiology</button>
  </div>

  <div class="projects-grid">
    {% for project in site.projects %}
      <div class="project-card" data-category="{{ project.category }}">
        <div class="project-header">
          <span class="project-category">{{ project.category | capitalize }}</span>
          <span class="project-index">No. {{ forloop.index | prepend: '00' | slice: -2, 2 }}</span>
        </div>
        <div class="project-body">
          <h2 class="project-title">{{ project.title }}</h2>
          <p class="project-excerpt">{{ project.excerpt | strip_html | truncate: 120 }}</p>
          <div class="project-meta">
            <span class="project-date">{{ project.date | date: "%B %Y" }}{% if project.presented_at %} &middot; {{ project.presented_at }}{% endif %}</span>
            <a href="{{ project.url | relative_url }}" class="read-more">View Details</a>
          </div>
        </div>
      </div>
    {% endfor %}
  </div>
</div>

<section class="cta-section">
  <div class="cta-content">
    <h2 class="cta-title">Want to talk about any of this?</h2>
    <p class="cta-text">Feel free to reach out. I'm always happy to chat about research or new ideas.</p>
    <a href="{{ '/' | relative_url }}#contact" class="cta-button">Get in touch</a>
  </div>
</section>