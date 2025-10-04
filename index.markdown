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
        <span class="eyebrow">Computational virologist &amp; designer</span>
        <h1>Crafting humane AI for antiviral discovery</h1>
        <p>
          I'm Alan "Hiyata" Carbajo Jr., architecting machine learning pipelines at Wayne State University School of Medicine with
          <a href="https://www.med.wayne.edu/profile/dx0934" target="_blank" rel="noopener">Dr. Phil Pellett</a>. I transform noisy genomic signals into visual stories,
          tools, and experimental hypotheses that help teams accelerate translational research.
        </p>
        <div class="typing-wrapper">
          <span class="typing-label">Currently exploring</span>
          <span class="typing-line" data-typing></span>
        </div>
        <div class="hero-actions">
          <a class="btn btn-primary" href="{{ '/projects' | relative_url }}">View recent work</a>
          <a class="btn btn-secondary" href="#contact">Request collaboration</a>
        </div>
        <ul class="hero-highlights">
          <li>Rapid diffusion-driven genome design experiments that surface interpretable motifs.</li>
          <li>Bridging wet-lab assays with adaptive machine learning frameworks for viral phenotyping.</li>
          <li>Designing immersive data stories that help clinicians, researchers, and funders align.</li>
        </ul>
        <ul class="hero-metrics">
          <li class="hero-metric" data-animate="fade-up" data-animate-delay="220">
            <span class="hero-metric-title">Years bridging ML &amp; design</span>
            <span class="hero-metric-value">8+</span>
            <span class="hero-metric-caption">Guiding translational teams from idea to deployable tooling.</span>
          </li>
          <li class="hero-metric" data-animate="fade-up" data-animate-delay="280">
            <span class="hero-metric-title">Impact experiments shipped</span>
            <span class="hero-metric-value">35</span>
            <span class="hero-metric-caption">Prototypes and studies aligning researchers, clinicians, and funders.</span>
          </li>
          <li class="hero-metric" data-animate="fade-up" data-animate-delay="340">
            <span class="hero-metric-title">Collaborative specialties</span>
            <span class="hero-metric-value">Genomics · HCI · AI ethics</span>
            <span class="hero-metric-caption">Shaping responsible systems for antiviral discovery.</span>
          </li>
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
          <div class="badge" data-animate="fade-up" data-animate-delay="320">
            <span class="badge-label">Collaborations</span>
            <p>Wayne State University School of Medicine Virology Lab.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section spotlight-section" id="spotlight">
    <div class="spotlight-inner">
      <div class="spotlight-lede" data-animate="fade-up">
        <span class="eyebrow">Signature workstreams</span>
        <h2>Where I create outsized value for research-driven teams</h2>
        <p>
          I specialise in the liminal space where machine learning, wet-lab practice, and human storytelling overlap.
          These workstreams help partners stand up durable platforms, validate hypotheses faster, and bring discoveries
          to the people who need them most.
        </p>
      </div>
      <div class="spotlight-grid">
        <article class="spotlight-card" data-animate="fade-up" data-animate-delay="120">
          <div class="spotlight-icon"><i class="fas fa-flask"></i></div>
          <h3>Integrated research platforms</h3>
          <p>
            Architecting secure, end-to-end systems that connect lab notebooks, data lakes, and visual dashboards for
            antiviral discovery teams.
          </p>
          <div class="spotlight-meta"><i class="fas fa-users"></i><span>Partnering with clinicians &amp; data scientists</span></div>
        </article>
        <article class="spotlight-card" data-animate="fade-up" data-animate-delay="200">
          <div class="spotlight-icon"><i class="fas fa-seedling"></i></div>
          <h3>Hypothesis prototyping sprints</h3>
          <p>
            Facilitating rapid cycles that pair generative models with lab assays to surface interpretable biomarkers
            and prioritise experiments.
          </p>
          <div class="spotlight-meta"><i class="fas fa-stopwatch"></i><span>Cutting iteration time from months to weeks</span></div>
        </article>
        <article class="spotlight-card" data-animate="fade-up" data-animate-delay="280">
          <div class="spotlight-icon"><i class="fas fa-lightbulb"></i></div>
          <h3>Story-led stakeholder alignment</h3>
          <p>
            Designing immersive narratives and decision rooms that help funders, researchers, and policymakers align on
            translational roadmaps.
          </p>
          <div class="spotlight-meta"><i class="fas fa-handshake"></i><span>From grant pitches to regulatory briefings</span></div>
        </article>
      </div>
    </div>
  </section>

  <section class="section about-section" id="about">
    <div class="section-header" data-animate="fade-up">
      <span class="eyebrow">About the journal</span>
      <h2>Exploring the intersection of artificial intelligence and virology</h2>
      <p>
        This journal documents living prototypes, experiments, and reflections from my studio inside the virology lab.
        Each entry distills how I pair computational intuition with wet-lab rigor to sketch antiviral tools, craft
        collaborations, and translate complex datasets into shared understanding.
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
    <div class="impact-grid">
      <article class="impact-card" data-animate="fade-up" data-animate-delay="60">
        <span class="impact-number">Lab-ready</span>
        <span class="impact-label">AI software ecosystems that guide virology experiments and decision-making.</span>
      </article>
      <article class="impact-card" data-animate="fade-up" data-animate-delay="140">
        <span class="impact-number">Atlas-scale</span>
        <span class="impact-label">Sequence intelligence frameworks connecting genomic design, surveillance, and insight.</span>
      </article>
      <article class="impact-card" data-animate="fade-up" data-animate-delay="220">
        <span class="impact-number">Story-led</span>
        <span class="impact-label">Collaborations shaped through narrative prototypes and facilitation across disciplines.</span>
      </article>
    </div>
    <div class="journey-timeline">
      <article class="journey-node" data-animate="fade-up" data-animate-delay="160">
        <span class="journey-year">2023 — Present</span>
        <h3>Wayne State University School of Medicine</h3>
        <p>
          Operating at the convergence of computational virology and interaction design—building decision systems that
          pair molecular data with narrative artefacts for clinicians and researchers.
        </p>
        <ul class="journey-tags">
          <li class="journey-tag">Deep learning</li>
          <li class="journey-tag">Wet-lab integration</li>
          <li class="journey-tag">Product strategy</li>
        </ul>
      </article>
      <article class="journey-node" data-animate="fade-up" data-animate-delay="240">
        <span class="journey-year">2019 — 2023</span>
        <h3>Translational AI experimentation</h3>
        <p>
          Led rapid prototyping sprints with biomedical teams to validate generative models, design hypothesis engines,
          and deploy visual analytics that shorten the loop between data, discovery, and action.
        </p>
        <ul class="journey-tags">
          <li class="journey-tag">Model prototyping</li>
          <li class="journey-tag">Team facilitation</li>
          <li class="journey-tag">Research enablement</li>
        </ul>
      </article>
      <article class="journey-node" data-animate="fade-up" data-animate-delay="320">
        <span class="journey-year">Earlier</span>
        <h3>Designing immersive science communication</h3>
        <p>
          Crafted interactive experiences for educators and storytellers that demystified complex biology, laying the
          foundation for empathetic communication across disciplines.
        </p>
        <ul class="journey-tags">
          <li class="journey-tag">Experience design</li>
          <li class="journey-tag">Narrative strategy</li>
          <li class="journey-tag">Systems thinking</li>
        </ul>
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
      <p>Insights on AI-driven biology, research tooling, and the craft of technical storytelling.</p>
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
        <span class="eyebrow">Let's collaborate</span>
        <h2>Have a project or research question in mind?</h2>
        <p>
          I'm always interested in partnering with scientists, engineers, and storytellers to craft meaningful tooling
          around viral research. Reach out and let's design something impactful together.
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
