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
        <span class="eyebrow">AI-driven virology insights</span>
        <h1>Designing intelligent systems for viral discovery</h1>
        <p>
          I'm Alan Carbajo, a researcher at Wayne State University School of Medicine
          working with <a href="https://biochemmicroimmuno.med.wayne.edu/profile/dx0934" target="_blank" rel="noopener">Dr. Phil Pellett</a> to
          explore how machine learning can accelerate breakthroughs in virology and genomic design.
        </p>
        <div class="typing-wrapper">
          <span class="typing-label">Currently exploring</span>
          <span class="typing-line" data-typing></span>
        </div>
        <div class="hero-actions">
          <a class="btn btn-primary" href="{{ '/projects' | relative_url }}">View recent work</a>
        </div>
        <ul class="hero-highlights">
          <li>Generative DNA design workflows guided by deep learning</li>
          <li>Predictive models that capture viral behavior and tropism</li>
          <li>Interactive data visualizations that tell scientific stories</li>
        </ul>
      </div>
      <div class="hero-visual" data-animate="fade-up" data-animate-delay="120">
        <div class="pdb-frame" aria-hidden="true">
          <div id="pdb-container" class="pdb-viewer"></div>
          <div class="pdb-glow"></div>
        </div>
        <div class="hero-badges">
          <div class="badge" data-animate="fade-up" data-animate-delay="220">
            <span class="badge-label">Latest focus</span>
            <p>Mapping latent genomic representations for antiviral discovery.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section about-section" id="about">
    <div class="section-header" data-animate="fade-up">
      <span class="eyebrow">About the journal</span>
      <h2>Exploring the intersection of artificial intelligence and virology</h2>
      <p>
        This journal documents experiments, prototypes, and reflections from my work designing computational tools for
        virology. I share lessons from the lab, notes from current projects, and ideas that push the boundaries of how
        we model and design biological systems.
      </p>
    </div>
    <div class="about-grid">
      <article class="about-card" data-animate="fade-up" data-animate-delay="120">
        <h3>Scientific storytelling</h3>
        <p>
          I translate complex datasets into intuitive visual narratives—bridging researchers, clinicians, and broader
          audiences with interactive dashboards and exploratory tools.
        </p>
      </article>
      <article class="about-card" data-animate="fade-up" data-animate-delay="200">
        <h3>Systems thinking</h3>
        <p>
          By combining genomics, epidemiology, and machine learning, I develop end-to-end workflows that move from raw
          sequencing data to actionable hypotheses and design insights.
        </p>
      </article>
    </div>
    <div class="focus-grid">
      <article class="focus-card" data-animate="fade-up">
        <i class="fas fa-brain"></i>
        <h3>Machine learning</h3>
        <p>Designing advanced models that learn latent viral patterns and predict phenotypic behavior.</p>
      </article>
      <article class="focus-card" data-animate="fade-up" data-animate-delay="120">
        <i class="fas fa-dna"></i>
        <h3>Viral genomics</h3>
        <p>Generating and analyzing viral genomes with neural networks for design and discovery.</p>
      </article>
      <article class="focus-card" data-animate="fade-up" data-animate-delay="200">
        <i class="fas fa-chart-line"></i>
        <h3>Epidemiology</h3>
        <p>Modeling population-level spread to inform responses during outbreaks and emerging threats.</p>
      </article>
    </div>
  </section>

  <section class="section projects-section" id="projects">
    <div class="section-header" data-animate="fade-up">
      <span class="eyebrow">Recent projects</span>
      <h2>Putting intelligent pipelines into practice</h2>
      <p>Selected work that blends computational research, design, and scientific communication.</p>
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
      <h2>Notes, experiments, and observations from the lab</h2>
      <p>Insights on AI-driven biology, research tooling, and the craft of storytelling.</p>
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
