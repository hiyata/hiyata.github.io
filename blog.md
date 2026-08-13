---
layout: default
title: Blog
permalink: /blog/
---

<header class="page-header">
  <div class="page-header-inner">
    <span class="kicker">Archive</span>
    <h1>Writing</h1>
    <p>Notes and reflections on AI-driven virology research.</p>
  </div>
</header>

<div class="blog-container">
  {% assign posts = site.posts %}
  {% if posts.size > 0 %}
  <div class="featured-post">
    {% assign featured = posts.first %}
    <span class="featured-label">Latest entry</span>
    <h2 class="featured-title"><a href="{{ featured.url | relative_url }}">{{ featured.title }}</a></h2>
    <p class="featured-meta">{{ featured.date | date: "%B %d, %Y" }}{% if featured.category %} &middot; {{ featured.category }}{% endif %}</p>
    <p class="featured-excerpt">{{ featured.excerpt | strip_html | truncatewords: 45 }}</p>
    <a href="{{ featured.url | relative_url }}" class="read-more-btn">Read full entry <span aria-hidden="true">&rarr;</span></a>
  </div>

  {% if posts.size > 1 %}
  <div class="blog-posts">
    {% for post in posts offset:1 %}
    <article class="blog-post">
      <span class="post-date">{{ post.date | date: "%b %d, %Y" }}</span>
      <h3 class="post-title"><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
      <p class="post-excerpt">{{ post.excerpt | strip_html | truncatewords: 25 }}</p>
      <a href="{{ post.url | relative_url }}" class="read-more">Continue reading <span aria-hidden="true">&rarr;</span></a>
    </article>
    {% endfor %}
  </div>
  {% endif %}
  {% else %}
  <p class="blog-empty">Nothing posted yet. Check back soon.</p>
  {% endif %}
</div>

<style>
  .blog-container {
    max-width: var(--content-width);
    margin: 0 auto;
    padding: clamp(2rem, 4vh, 2.75rem) max(1.5rem, 4vw) 4rem;
  }

  .blog-empty {
    color: var(--ink-faint);
    font-size: 0.95rem;
  }

  .featured-post {
    padding: 1.5rem 1.75rem;
    border-radius: var(--radius-md);
    background: var(--surface);
    border: 1px solid var(--border);
    margin-bottom: 1.75rem;
  }

  .featured-label {
    font-family: var(--mono);
    color: var(--accent);
    font-size: 0.72rem;
    text-transform: uppercase;
    font-weight: 700;
    letter-spacing: 0.06em;
  }

  .featured-title {
    font-family: var(--serif);
    font-size: 1.6rem;
    font-weight: 700;
    margin: 0.6rem 0 0.35rem;
    line-height: 1.25;
  }

  .featured-title a {
    color: var(--ink);
    text-decoration: none;
    transition: color 0.2s ease;
  }

  .featured-title a:hover {
    color: var(--accent);
  }

  .featured-meta {
    font-family: var(--mono);
    font-size: 0.78rem;
    color: var(--ink-faint);
    margin: 0 0 0.9rem;
  }

  .featured-excerpt {
    color: var(--ink-soft);
    font-size: 0.98rem;
    line-height: 1.65;
    margin-bottom: 1.25rem;
  }

  .read-more-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    padding: 0.6rem 1.1rem;
    border-radius: var(--radius-sm);
    background: var(--ink);
    color: #fff;
    text-decoration: none;
    font-size: 0.85rem;
    font-weight: 600;
    transition: background-color 0.2s ease;
  }

  .read-more-btn:hover {
    background: var(--accent);
  }

  .blog-posts {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 1rem;
  }

  .blog-post {
    padding: 1.25rem;
    border-radius: var(--radius-md);
    background: var(--surface);
    border: 1px solid var(--border);
    transition: border-color 0.2s ease, transform 0.2s ease;
  }

  .blog-post:hover {
    border-color: var(--border-strong);
    transform: translateY(-2px);
  }

  .post-date {
    font-family: var(--mono);
    font-size: 0.72rem;
    color: var(--ink-faint);
  }

  .post-title {
    margin: 0.5rem 0 0.5rem;
    font-size: 1.05rem;
    font-weight: 700;
    line-height: 1.3;
  }

  .post-title a {
    color: var(--ink);
    text-decoration: none;
    transition: color 0.2s ease;
  }

  .post-title a:hover {
    color: var(--accent);
  }

  .post-excerpt {
    color: var(--ink-soft);
    font-size: 0.9rem;
    line-height: 1.6;
    margin-bottom: 0.9rem;
  }

  .read-more {
    display: inline-flex;
    color: var(--ink);
    text-decoration: none;
    font-size: 0.82rem;
    font-weight: 600;
  }

  .read-more:hover {
    color: var(--accent);
  }
</style>
