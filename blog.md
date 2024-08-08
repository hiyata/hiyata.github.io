---
layout: default
title: Blog
permalink: /blog/
---

<div class="blog-container">
  <h1 class="blog-title">My Blog</h1>
  <div class="blog-posts">
    {% for post in site.posts %}
      <div class="blog-post" data-post-id="{{ forloop.index }}">
        <div class="post-date">
          <span class="day">{{ post.date | date: "%d" }}</span>
          <span class="month">{{ post.date | date: "%b" }}</span>
        </div>
        <div class="post-content">
          <h2 class="post-title"><a href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a></h2>
          <p class="post-excerpt">{{ post.excerpt | strip_html | truncatewords: 30 }}</p>
          <a href="{{ post.url | prepend: site.baseurl }}" class="read-more">Read More</a>
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
    max-width: 800px;
    margin: 0 auto;
    padding: 2rem;
    font-family: 'Arial', sans-serif;
  }

  .blog-title {
    text-align: center;
    font-size: 3rem;
    color: #333;
    margin-bottom: 2rem;
  }

  .blog-posts {
    display: grid;
    gap: 2rem;
  }

  .blog-post {
    display: flex;
    background-color: #fff;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease;
  }

  .blog-post:hover {
    transform: translateY(-5px);
  }

  .post-date {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 1rem;
    background-color: #3498db;
    color: #fff;
    font-weight: bold;
    text-align: center;
    min-width: 80px;
  }

  .post-date .day {
    font-size: 1.5rem;
  }

  .post-date .month {
    font-size: 0.9rem;
    text-transform: uppercase;
  }

  .post-content {
    padding: 1.5rem;
    flex-grow: 1;
  }

  .post-title {
    margin: 0 0 1rem;
    font-size: 1.5rem;
  }

  .post-title a {
    color: #333;
    text-decoration: none;
    transition: color 0.3s ease;
  }

  .post-title a:hover {
    color: #3498db;
  }

  .post-excerpt {
    color: #666;
    font-size: 0.9rem;
    line-height: 1.6;
    margin-bottom: 1rem;
  }

  .read-more {
    display: inline-block;
    padding: 0.5rem 1rem;
    background-color: #3498db;
    color: #fff;
    text-decoration: none;
    border-radius: 4px;
    font-size: 0.9rem;
    transition: background-color 0.3s ease;
  }

  .read-more:hover {
    background-color: #2980b9;
  }

  .pagination {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 2rem;
  }

  .pagination-btn {
    padding: 0.5rem 1rem;
    background-color: #3498db;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 0.9rem;
    transition: background-color 0.3s ease;
  }

  .pagination-btn:hover {
    background-color: #2980b9;
  }

  #page-number {
    margin: 0 1rem;
    font-size: 0.9rem;
  }
</style>

<script src="https://cdnjs.cloudflare.com/ajax/libs/animejs/3.2.1/anime.min.js"></script>
<script>
  document.addEventListener('DOMContentLoaded', () => {
    const postsPerPage = 5;
    const posts = document.querySelectorAll('.blog-post');
    let currentPage = 1;
    const totalPages = Math.ceil(posts.length / postsPerPage);

    function showPage(page) {
      const start = (page - 1) * postsPerPage;
      const end = start + postsPerPage;

      posts.forEach((post, index) => {
        if (index >= start && index < end) {
          post.style.display = 'flex';
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

    // Animate blog title
    anime({
      targets: '.blog-title',
      opacity: [0, 1],
      translateY: [-50, 0],
      easing: 'easeOutExpo',
      duration: 1200
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