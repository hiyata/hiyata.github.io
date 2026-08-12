---
layout: default
title: Blog
permalink: /blog/
---

<div class="blog-container">
  <h1 class="blog-title">Writing</h1>
  <p class="blog-subtitle">Notes and reflections on AI-driven virology research</p>
  
  <div class="featured-post">
    {% for post in site.posts limit:1 %}
      <div class="featured-post-content">
        <span class="featured-label">Featured Post</span>
        <h2 class="featured-title"><a href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a></h2>
        <p class="featured-excerpt">{{ post.excerpt | strip_html | truncatewords: 50 }}</p>
        <a href="{{ post.url | prepend: site.baseurl }}" class="read-more-btn">Read Full Article</a>
      </div>
      <div class="featured-post-image" style="background-image: url('{{ post.featured_image | default: "/assets/images/default-featured.jpg" }}');"></div>
    {% endfor %}
  </div>

  <div class="blog-posts">
    {% for post in site.posts offset:1 %}
      <div class="blog-post" data-post-id="{{ forloop.index }}">
        <div class="post-image" style="background-image: url('{{ post.thumbnail | default: "/assets/images/default-thumbnail.jpg" }}');"></div>
        <div class="post-content">
          <div class="post-meta">
            <span class="post-date">{{ post.date | date: "%b %d, %Y" }}</span>
            <span class="post-category">{{ post.category }}</span>
          </div>
          <h2 class="post-title"><a href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a></h2>
          <p class="post-excerpt">{{ post.excerpt | strip_html | truncatewords: 25 }}</p>
          <a href="{{ post.url | prepend: site.baseurl }}" class="read-more">Continue Reading</a>
        </div>
      </div>
    {% endfor %}
  </div>
</div>

<div class="pagination">
  <button id="prev-page" class="pagination-btn">&larr; Previous</button>
  <span id="page-number">Page 1</span>
  <button id="next-page" class="pagination-btn">Next &rarr;</button>
</div>

<style>
  .blog-container {
    max-width: 1080px;
    margin: 0 auto;
    padding: 3rem 1.5rem 5rem;
  }

  .blog-title {
    text-align: left;
    font-size: 2.5rem;
    font-style: italic;
    color: var(--ink);
    margin-bottom: 0.5rem;
    font-weight: 600;
  }

  .blog-subtitle {
    text-align: left;
    font-size: 1.05rem;
    color: var(--ink-soft);
    margin-bottom: 3rem;
    padding-bottom: 2rem;
    border-bottom: 1px solid var(--rule);
  }

  .featured-post {
    display: flex;
    gap: 2.5rem;
    margin-bottom: 3.5rem;
    padding-bottom: 3.5rem;
    border-bottom: 1px solid var(--rule);
  }

  .featured-post-content {
    flex: 1;
  }

  .featured-label {
    color: var(--accent);
    font-family: var(--mono);
    font-size: 0.72rem;
    text-transform: uppercase;
    font-weight: 500;
    letter-spacing: 0.1em;
  }

  .featured-title {
    font-size: 1.9rem;
    font-style: italic;
    font-weight: 600;
    margin: 0.75rem 0;
  }

  .featured-title a {
    color: var(--ink);
    text-decoration: none;
    transition: color 0.2s ease;
  }

  .featured-title a:hover {
    color: var(--accent);
  }

  .featured-excerpt {
    color: var(--ink-soft);
    font-size: 1.05rem;
    line-height: 1.7;
    margin-bottom: 1.5rem;
  }

  .featured-post-image {
    flex: 0 0 280px;
    aspect-ratio: 4 / 3;
    background-size: cover;
    background-position: center;
    border: 1px solid var(--rule);
  }

  .read-more-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    color: var(--ink);
    text-decoration: none;
    font-family: var(--mono);
    font-size: 0.78rem;
    font-weight: 500;
    letter-spacing: 0.04em;
    border-bottom: 1px solid var(--rule-strong);
    transition: color 0.2s ease, border-color 0.2s ease;
  }

  .read-more-btn:hover {
    color: var(--accent);
    border-color: var(--accent);
  }

  .blog-posts {
    display: grid;
    grid-template-columns: 1fr;
    gap: 0;
    border-top: 1px solid var(--rule);
  }

  .blog-post {
    display: flex;
    gap: 2rem;
    padding: 2rem 0;
    border-bottom: 1px solid var(--rule);
  }

  .post-image {
    flex: 0 0 160px;
    aspect-ratio: 4 / 3;
    background-size: cover;
    background-position: center;
    border: 1px solid var(--rule);
  }

  .post-content {
    flex: 1;
    padding: 0;
  }

  .post-meta {
    display: flex;
    gap: 1rem;
    align-items: center;
    margin-bottom: 0.75rem;
    font-family: var(--mono);
    font-size: 0.75rem;
    letter-spacing: 0.04em;
    color: var(--ink-faint);
  }

  .post-category {
    text-transform: uppercase;
    color: var(--accent);
  }

  .post-title {
    margin: 0 0 0.6rem;
    font-size: 1.3rem;
    font-style: italic;
    font-weight: 600;
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
    font-size: 0.98rem;
    line-height: 1.65;
    margin-bottom: 0.85rem;
  }

  .read-more {
    display: inline-flex;
    color: var(--ink);
    text-decoration: none;
    font-family: var(--mono);
    font-size: 0.75rem;
    font-weight: 500;
    letter-spacing: 0.04em;
    border-bottom: 1px solid var(--rule-strong);
    transition: color 0.2s ease, border-color 0.2s ease;
  }

  .read-more:hover {
    color: var(--accent);
    border-color: var(--accent);
  }

  .pagination {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 3rem;
  }

  .pagination-btn {
    padding: 0.6rem 1.25rem;
    background: transparent;
    color: var(--ink);
    border: 1px solid var(--ink);
    cursor: pointer;
    font-family: var(--mono);
    font-size: 0.78rem;
    font-weight: 500;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    transition: background-color 0.2s ease, color 0.2s ease;
  }

  .pagination-btn:hover {
    background: var(--ink);
    color: var(--paper);
  }

  #page-number {
    margin: 0 1.5rem;
    font-family: var(--mono);
    font-size: 0.85rem;
    color: var(--ink-soft);
  }

  @media (max-width: 768px) {
    .featured-post {
      flex-direction: column-reverse;
    }

    .featured-post-image {
      flex-basis: auto;
      height: 220px;
    }

    .blog-post {
      flex-direction: column;
    }

    .post-image {
      flex-basis: auto;
      height: 180px;
      width: 100%;
    }
  }
</style>

<script>
  document.addEventListener('DOMContentLoaded', () => {
    const postsPerPage = 6;
    const posts = document.querySelectorAll('.blog-post');
    let currentPage = 1;
    const totalPages = Math.ceil(posts.length / postsPerPage);

    function showPage(page) {
      const start = (page - 1) * postsPerPage;
      const end = start + postsPerPage;

      posts.forEach((post, index) => {
        if (index >= start && index < end) {
          post.style.display = 'block';
        } else {
          post.style.display = 'none';
        }
      });

      document.getElementById('page-number').textContent = `Page ${page} of ${totalPages}`;
      
      anime({
        targets: '.blog-post',
        opacity: [0, 1],
        translateY: [20, 0],
        easing: 'easeOutExpo',
        duration: 800,
        delay: anime.stagger(100)
      });
    }

    document.getElementById('prev-page').addEventListener('click', () => {
      if (currentPage > 1) {
        currentPage--;
        showPage(currentPage);
      }
    });

    document.getElementById('next-page').addEventListener('click', () => {
      if (currentPage < totalPages) {
        currentPage++;
        showPage(currentPage);
      }
    });

    showPage(currentPage);

    // Animate blog title and subtitle
    anime({
      targets: ['.blog-title', '.blog-subtitle'],
      opacity: [0, 1],
      translateY: [-30, 0],
      easing: 'easeOutExpo',
      duration: 1200,
      delay: anime.stagger(200)
    });

    // Animate featured post
    anime({
      targets: '.featured-post',
      opacity: [0, 1],
      translateY: [50, 0],
      easing: 'easeOutExpo',
      duration: 1000,
      delay: 300
    });

    // Animate post appearance on scroll
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const postId = entry.target.getAttribute('data-post-id');
          anime({
            targets: entry.target,
            opacity: [0, 1],
            translateY: [50, 0],
            easing: 'easeOutExpo',
            duration: 800,
            delay: postId * 100
          });
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });

    posts.forEach(post => {
      observer.observe(post);
    });
  });
</script>