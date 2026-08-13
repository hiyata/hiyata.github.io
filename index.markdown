---
layout: default
title: Welcome
custom_css: home
custom_js: home
---

<div id="loading-overlay" class="loading-overlay" aria-hidden="true">
  <div class="loading-spinner" role="status" aria-label="Loading"></div>
</div>

<main class="home-viewport" id="content">
  <section class="hero-section" id="home">
    <div class="hero-grid">
      <div class="hero-copy" data-animate="fade-up">
        <span class="eyebrow">AI &amp; virology</span>
        <h1>Hi, I'm Alan — I use machine learning to study viruses</h1>
        <p>
          I'm a researcher at Wayne State University School of Medicine, working with
          <a href="https://biochemmicroimmuno.med.wayne.edu/profile/dx0934" target="_blank" rel="noopener">Dr. Phil Pellett</a>
          on ways to apply machine learning to virology and genomics. This site is where I keep track of what I'm building and learning along the way.
        </p>
        <div class="typing-wrapper">
          <span class="typing-label">Currently exploring</span>
          <span class="typing-line" data-typing></span>
        </div>
        <div class="hero-actions">
          <a class="btn btn-primary" href="{{ '/projects' | relative_url }}">See what I've been working on</a>
        </div>
        <ul class="hero-highlights">
          <li>Generating artificial viral genomes with deep learning</li>
          <li>Building models that predict how viruses behave</li>
          <li>Making the data easier to look at and explore</li>
        </ul>
      </div>
      <div class="hero-visual" data-animate="fade-up" data-animate-delay="120">
        <div class="pdb-frame" aria-hidden="true">
          <div id="pdb-container" class="pdb-viewer"></div>
          <div class="pdb-glow"></div>
        </div>
        <div class="hero-badges">
          <div class="badge" data-animate="fade-up" data-animate-delay="220">
            <span class="badge-label">Right now I'm</span>
            <p>Trying to map how viral genomes relate to each other so I can spot patterns worth digging into.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section about-section" id="about">
    <div class="section-header" data-animate="fade-up">
      <span class="eyebrow">About this site</span>
      <h2>A place to keep track of what I'm working on</h2>
      <p>
        This is basically my lab notebook, public. I write up experiments and side projects as I go, mostly around
        AI and virology, partly to keep myself honest and partly because I like sharing this stuff.
      </p>
    </div>
    <div class="about-grid">
      <article class="about-card" data-animate="fade-up" data-animate-delay="120">
        <h3>Making data make sense</h3>
        <p>
          I like turning messy datasets into visuals and tools that are actually pleasant to explore — for myself
          as much as for anyone else who's curious.
        </p>
      </article>
      <article class="about-card" data-animate="fade-up" data-animate-delay="200">
        <h3>Connecting the dots</h3>
        <p>
          I try to pull together genomics, epidemiology, and machine learning to go from raw sequencing data
          to something I can actually learn from.
        </p>
      </article>
    </div>
    <div class="focus-grid">
      <article class="focus-card" data-animate="fade-up">
        <i class="fas fa-brain"></i>
        <h3>Machine learning</h3>
        <p>Building models that pick up on viral patterns and try to predict how a virus behaves.</p>
      </article>
      <article class="focus-card" data-animate="fade-up" data-animate-delay="120">
        <i class="fas fa-dna"></i>
        <h3>Viral genomics</h3>
        <p>Generating and analyzing viral genomes with neural networks, mostly out of curiosity about what's possible.</p>
      </article>
      <article class="focus-card" data-animate="fade-up" data-animate-delay="200">
        <i class="fas fa-chart-line"></i>
        <h3>Epidemiology</h3>
        <p>Modeling how outbreaks spread, and what that might tell us before the next one.</p>
      </article>
    </div>
  </section>

  <section class="section projects-section" id="projects">
    <div class="section-header" data-animate="fade-up">
      <span class="eyebrow">Recent projects</span>
      <h2>A few things I've been building</h2>
      <p>Some of the projects I've worked on, mixing research with a bit of design and storytelling.</p>
    </div>
    <div class="cards-grid">
      {% for project in site.projects limit:3 %}
      <article class="project-card" data-animate="fade-up" data-animate-delay="{{ forloop.index0 | times: 120 }}">
        <div class="project-card-body">
          <h3><a href="{{ project.url | relative_url }}">{{ project.title }}</a></h3>
          <p>{{ project.excerpt | strip_html | truncatewords: 28 }}</p>
        </div>
        <div class="project-card-footer">
          {% if project.presented_at %}
          <span class="project-tag">{{ project.presented_at }}</span>
          {% endif %}
          <a class="project-link" href="{{ project.url | relative_url }}" aria-label="Read more about {{ project.title }}">
            View project
            <span aria-hidden="true">→</span>
          </a>
        </div>
      </article>
      {% endfor %}
    </div>
    <div class="section-cta" data-animate="fade-up" data-animate-delay="360">
      <a class="btn btn-primary" href="{{ '/projects' | relative_url }}">Explore all projects</a>
    </div>
  </section>

  <section class="section blog-section" id="blog">
    <div class="section-header" data-animate="fade-up">
      <span class="eyebrow">Latest writing</span>
      <h2>Notes from the lab</h2>
      <p>Things I've learned or thought about while working on AI and biology.</p>
    </div>
    <div class="cards-grid">
      {% for post in site.posts limit:2 %}
      <article class="blog-card" data-animate="fade-up" data-animate-delay="{{ forloop.index0 | times: 120 }}">
        <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
        <p>{{ post.excerpt | strip_html | truncatewords: 30 }}</p>
        <span class="blog-meta">Published {{ post.date | date: "%B %d, %Y" }}</span>
        <a class="blog-link" href="{{ post.url | relative_url }}" aria-label="Read {{ post.title }}">
          Read article
          <span aria-hidden="true">→</span>
        </a>
      </article>
      {% endfor %}
    </div>
    <div class="section-cta" data-animate="fade-up" data-animate-delay="260">
      <a class="btn btn-secondary" href="{{ '/blog' | relative_url }}">Browse the archive</a>
    </div>
  </section>

  <section class="section contact-section" id="contact">
    <div class="contact-card" data-animate="fade-up">
      <div>
        <span class="eyebrow">Contact</span>
        <h2>Get in touch</h2>
        <p>
          Have a question or want to say hello? I’d love to hear from you.
        </p>
      </div>
      <div class="contact-actions">
        <a class="btn btn-primary" href="mailto:{{ site.email }}">Email me</a>
        <a class="btn btn-secondary" href="https://www.linkedin.com/in/alan-luis-carbajo-jr-9929b7138" target="_blank" rel="noopener">Connect on LinkedIn</a>
      </div>
    </div>
  </section>
</main>

<script src="https://3Dmol.csb.pitt.edu/build/3Dmol-min.js"></script>
