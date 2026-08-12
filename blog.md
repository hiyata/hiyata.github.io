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
    padding: 2.5rem 1.5rem 4rem;
  }

  .blog-title {
    text-align: left;
    font-size: 2.25rem;
    color: var(--ink);
    margin-bottom: 0.4rem;
    font-weight: 800;
  }

  .blog-subtitle {
    text-align: left;
    font-size: 1rem;
    color: var(--ink-soft);
    margin-bottom: 2.5rem;
  }

  .featured-post {
    display: flex;
    gap: 2rem;
    margin-bottom: 2rem;
    padding: 1.5rem;
    border-radius: 14px;
    background: var(--surface-muted);
    border: 1px solid var(--border);
  }

  .featured-post-content {
    flex: 1;
  }

  .featured-label {
    color: var(--accent);
    font-size: 0.75rem;
    text-transform: uppercase;
    font-weight: 700;
    letter-spacing: 0.05em;
  }

  .featured-title {
    font-size: 1.7rem;
    font-weight: 800;
    margin: 0.6rem 0;
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
    font-size: 1rem;
    line-height: 1.65;
    margin-bottom: 1.25rem;
  }

  .featured-post-image {
    flex: 0 0 260px;
    aspect-ratio: 4 / 3;
    background-size: cover;
    background-position: center;
    border-radius: 10px;
    border: 1px solid var(--border);
  }

  .read-more-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    padding: 0.6rem 1.1rem;
    border-radius: 8px;
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
    grid-template-columns: 1fr;
    gap: 1rem;
  }

  .blog-post {
    display: flex;
    gap: 1.5rem;
    padding: 1.25rem;
    border-radius: 12px;
    background: var(--surface);
    border: 1px solid var(--border);
    transition: border-color 0.2s ease;
  }

  .blog-post:hover {
    border-color: var(--border-strong);
  }

  .post-image {
    flex: 0 0 150px;
    aspect-ratio: 4 / 3;
    background-size: cover;
    background-position: center;
    border-radius: 8px;
    border: 1px solid var(--border);
  }

  .post-content {
    flex: 1;
    padding: 0;
  }

  .post-meta {
    display: flex;
    gap: 0.75rem;
    align-items: center;
    margin-bottom: 0.6rem;
    font-size: 0.8rem;
    color: var(--ink-faint);
  }

  .post-category {
    text-transform: uppercase;
    font-weight: 700;
    font-size: 0.72rem;
    color: var(--accent);
    background: rgba(194, 65, 12, 0.08);
    padding: 0.15rem 0.5rem;
    border-radius: 6px;
  }

  .post-title {
    margin: 0 0 0.5rem;
    font-size: 1.15rem;
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
    font-size: 0.92rem;
    line-height: 1.6;
    margin-bottom: 0.75rem;
  }

  .read-more {
    display: inline-flex;
    color: var(--ink);
    text-decoration: none;
    font-size: 0.85rem;
    font-weight: 600;
  }

  .read-more:hover {
    color: var(--accent);
  }

  .pagination {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 2.5rem;
  }

  .pagination-btn {
    padding: 0.55rem 1.1rem;
    background: transparent;
    color: var(--ink);
    border: 1px solid var(--border-strong);
    border-radius: 8px;
    cursor: pointer;
    font-size: 0.85rem;
    font-weight: 600;
    transition: background-color 0.2s ease, color 0.2s ease;
  }

  .pagination-btn:hover {
    background: var(--ink);
    color: #fff;
    border-color: var(--ink);
  }

  #page-number {
    margin: 0 1.25rem;
    font-size: 0.88rem;
    color: var(--ink-soft);
  }

  @media (max-width: 768px) {
    .featured-post {
      flex-direction: column-reverse;
    }

    .featured-post-image {
      flex-basis: auto;
      height: 200px;
    }

    .blog-post {
      flex-direction: column;
    }

    .post-image {
      flex-basis: auto;
      height: 160px;
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