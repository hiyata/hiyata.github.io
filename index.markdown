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
  <section class="masthead" id="home">
    <div class="masthead-grid">
      <div class="masthead-copy" data-animate="fade-up">
        <span class="kicker">Entry 001 — Welcome</span>
        <h1>Hi, I'm Alan — I predict which viruses can infect humans, from genome sequence alone</h1>
        <p>
          I'm a researcher at Wayne State University School of Medicine, working with
          <a href="https://biochemmicroimmuno.med.wayne.edu/profile/dx0934" target="_blank" rel="noopener">Dr. Phil Pellett</a>.
          Most recently, that meant building a 58,046-genome dataset across 15 virus families and training neural
          networks on raw k-mer frequency — no alignment, no annotation — to tell human-infecting viruses from
          everything else. This site is where I keep track of what I'm building and learning along the way.
        </p>
        <div class="hero-actions">
          <a class="btn btn-primary" href="{{ '/projects' | relative_url }}">See what I've been working on</a>
          <a class="btn btn-secondary" href="mailto:{{ site.email }}">Get in touch</a>
        </div>
      </div>
      <aside class="field-card" data-animate="fade-up" data-animate-delay="120">
        <div class="pdb-frame" aria-hidden="true">
          <div id="pdb-container" class="pdb-viewer"></div>
        </div>
        <p class="field-card-caption">Fig. 1 — an artificially generated Hepatitis B ORF1 structure</p>
        <dl class="field-notes">
          <div class="field-row">
            <dt>Institution</dt>
            <dd>Wayne State University SOM</dd>
          </div>
          <div class="field-row">
            <dt>Advisor</dt>
            <dd>Dr. Phil Pellett</dd>
          </div>
          <div class="field-row">
            <dt>Focus</dt>
            <dd>Host-range prediction from sequence</dd>
          </div>
          <div class="field-row">
            <dt>Exploring</dt>
            <dd><span class="typing-line" data-typing></span></dd>
          </div>
        </dl>
      </aside>
    </div>
  </section>

  <section class="section" id="about">
    <div class="section-grid">
      <div class="section-index" data-animate="fade-up">
        <span class="section-number">01</span>
        <span class="section-label">About</span>
      </div>
      <div class="section-body">
        <h2>A place to keep track of what I'm working on</h2>
        <p class="section-lede">
          This is basically my lab notebook, public. I write up experiments and side projects as I go, mostly around
          AI and virology, partly to keep myself honest and partly because I like sharing this stuff.
        </p>
        <div class="about-grid">
          <article class="about-card" data-animate="fade-up">
            <span class="about-card-num">A</span>
            <h3>Building datasets worth training on</h3>
            <p>
              GenBank's metadata is a mess — inconsistent host labels, missing fields, free-text notes. I built a
              three-tier pipeline (string matching, pattern lookup, then an LLM for the ambiguous cases) to turn
              82,513 raw genomes into a clean, host-labeled set of 58,046.
            </p>
          </article>
          <article class="about-card" data-animate="fade-up" data-animate-delay="80">
            <span class="about-card-num">B</span>
            <h3>Reading the model's reasoning</h3>
            <p>
              Predicting host compatibility is only half the point. I ablate individual k-mers to see which ones
              actually move the needle, then map those back onto genes to find out what the model is really
              picking up on.
            </p>
          </article>
        </div>
        <div class="focus-grid">
          <article class="focus-card" data-animate="fade-up">
            <span class="focus-card-tag">ML</span>
            <h3>Host-range prediction</h3>
            <p>Neural nets on k-mer frequency vectors (k = 3 to 8) beat logistic regression and random forest baselines at telling human-infecting viruses from the rest.</p>
          </article>
          <article class="focus-card" data-animate="fade-up" data-animate-delay="80">
            <span class="focus-card-tag">DNA</span>
            <h3>Genome generation</h3>
            <p>Projects like MambaVirus and SOMBRA that generate and simulate viral genomes, rather than just classify existing ones.</p>
          </article>
          <article class="focus-card" data-animate="fade-up" data-animate-delay="160">
            <span class="focus-card-tag">EPI</span>
            <h3>Adaptation over time</h3>
            <p>Tracked SARS-CoV-2's predicted human-adaptation signal drifting upward across 8,683 genomes from 2019 to 2024.</p>
          </article>
        </div>
      </div>
    </div>
  </section>

  <section class="section section-muted" id="projects">
    <div class="section-grid">
      <div class="section-index" data-animate="fade-up">
        <span class="section-number">02</span>
        <span class="section-label">Projects</span>
      </div>
      <div class="section-body">
        <div class="section-body-head">
          <h2>A few things I've been building</h2>
          <a class="section-body-link" href="{{ '/projects' | relative_url }}">All projects <span aria-hidden="true">&rarr;</span></a>
        </div>
        <p class="section-lede">Some of the projects I've worked on, mixing research with a bit of design and storytelling.</p>
        <div class="cards-grid">
          {% for project in site.projects limit:3 %}
          <article class="project-card" data-animate="fade-up" data-animate-delay="{{ forloop.index0 | times: 80 }}">
            <div class="project-card-body">
              <h3><a href="{{ project.url | relative_url }}">{{ project.title }}</a></h3>
              <p>{{ project.excerpt | strip_html | truncatewords: 24 }}</p>
            </div>
            <div class="project-card-footer">
              {% if project.presented_at %}
              <span class="project-tag">{{ project.presented_at }}</span>
              {% else %}
              <span></span>
              {% endif %}
              <a class="project-link" href="{{ project.url | relative_url }}" aria-label="Read more about {{ project.title }}">
                View <span aria-hidden="true">&rarr;</span>
              </a>
            </div>
          </article>
          {% endfor %}
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="blog">
    <div class="section-grid">
      <div class="section-index" data-animate="fade-up">
        <span class="section-number">03</span>
        <span class="section-label">Writing</span>
      </div>
      <div class="section-body">
        <div class="section-body-head">
          <h2>Notes from the lab</h2>
          <a class="section-body-link" href="{{ '/blog' | relative_url }}">Archive <span aria-hidden="true">&rarr;</span></a>
        </div>
        <p class="section-lede">Things I've learned or thought about while working on AI and biology.</p>
        <div class="cards-grid cards-grid-wide">
          {% for post in site.posts limit:2 %}
          <article class="blog-card" data-animate="fade-up" data-animate-delay="{{ forloop.index0 | times: 80 }}">
            <span class="blog-meta">{{ post.date | date: "%b %d, %Y" }}</span>
            <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
            <p>{{ post.excerpt | strip_html | truncatewords: 30 }}</p>
            <a class="blog-link" href="{{ post.url | relative_url }}" aria-label="Read {{ post.title }}">
              Read <span aria-hidden="true">&rarr;</span>
            </a>
          </article>
          {% endfor %}
        </div>
      </div>
    </div>
  </section>

  <section class="section section-muted contact-section" id="contact">
    <div class="section-grid">
      <div class="section-index" data-animate="fade-up">
        <span class="section-number">04</span>
        <span class="section-label">Contact</span>
      </div>
      <div class="section-body">
        <div class="contact-row" data-animate="fade-up">
          <div>
            <h2>Get in touch</h2>
            <p class="section-lede">Have a question or want to say hello? I'd love to hear from you.</p>
          </div>
          <div class="contact-actions">
            <a class="btn btn-primary" href="mailto:{{ site.email }}">Email me</a>
            <a class="btn btn-secondary" href="https://www.linkedin.com/in/alan-luis-carbajo-jr-9929b7138" target="_blank" rel="noopener">Connect on LinkedIn</a>
          </div>
        </div>
      </div>
    </div>
  </section>
</main>

<script src="https://3Dmol.csb.pitt.edu/build/3Dmol-min.js"></script>
