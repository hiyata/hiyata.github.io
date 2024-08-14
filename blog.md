---
layout: default
title: Blog
permalink: /blog/
---

<div class="blog-container">
  <h1 class="blog-title">Insights & Innovations</h1>
  <p class="blog-subtitle">Exploring the frontiers of science and technology</p>
  
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
    max-width: 1200px;
    margin: 0 auto;
    padding: 4rem 2rem;
    font-family: 'Roboto', sans-serif;
  }

  .blog-title {
    text-align: center;
    font-size: 3.5rem;
    color: #2c3e50;
    margin-bottom: 0.5rem;
    font-weight: 700;
  }

  .blog-subtitle {
    text-align: center;
    font-size: 1.2rem;
    color: #7f8c8d;
    margin-bottom: 3rem;
  }

  .featured-post {
    display: flex;
    background-color: #fff;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
    margin-bottom: 4rem;
  }

  .featured-post-content {
    flex: 1;
    padding: 3rem;
  }

  .featured-label {
    background-color: #e74c3c;
    color: #fff;
    padding: 0.3rem 0.8rem;
    border-radius: 20px;
    font-size: 0.8rem;
    text-transform: uppercase;
    font-weight: 600;
    letter-spacing: 1px;
  }

  .featured-title {
    font-size: 2.2rem;
    margin: 1rem 0;
  }

  .featured-title a {
    color: #2c3e50;
    text-decoration: none;
    transition: color 0.3s ease;
  }

  .featured-title a:hover {
    color: #e74c3c;
  }

  .featured-excerpt {
    color: #34495e;
    font-size: 1.1rem;
    line-height: 1.6;
    margin-bottom: 1.5rem;
  }

  .featured-post-image {
    flex: 1;
    background-size: cover;
    background-position: center;
  }

  .read-more-btn {
    display: inline-block;
    padding: 0.8rem 1.5rem;
    background-color: #3498db;
    color: #fff;
    text-decoration: none;
    border-radius: 30px;
    font-weight: 600;
    transition: background-color 0.3s ease;
  }

  .read-more-btn:hover {
    background-color: #2980b9;
  }

  .blog-posts {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 2rem;
  }

  .blog-post {
    background-color: #fff;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
  }

  .blog-post:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
  }

  .post-image {
    height: 200px;
    background-size: cover;
    background-position: center;
  }

  .post-content {
    padding: 1.5rem;
  }

  .post-meta {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1rem;
    font-size: 0.9rem;
    color: #7f8c8d;
  }

  .post-category {
    background-color: #2ecc71;
    color: #fff;
    padding: 0.2rem 0.6rem;
    border-radius: 15px;
    font-size: 0.8rem;
  }

  .post-title {
    margin: 0 0 1rem;
    font-size: 1.5rem;
    line-height: 1.3;
  }

  .post-title a {
    color: #2c3e50;
    text-decoration: none;
    transition: color 0.3s ease;
  }

  .post-title a:hover {
    color: #3498db;
  }

  .post-excerpt {
    color: #34495e;
    font-size: 0.95rem;
    line-height: 1.6;
    margin-bottom: 1rem;
  }

  .read-more {
    display: inline-block;
    padding: 0.5rem 1rem;
    background-color: #3498db;
    color: #fff;
    text-decoration: none;
    border-radius: 20px;
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
    margin-top: 3rem;
  }

  .pagination-btn {
    padding: 0.8rem 1.5rem;
    background-color: #3498db;
    color: #fff;
    border: none;
    border-radius: 30px;
    cursor: pointer;
    font-size: 1rem;
    font-weight: 600;
    transition: background-color 0.3s ease;
  }

  .pagination-btn:hover {
    background-color: #2980b9;
  }

  #page-number {
    margin: 0 1.5rem;
    font-size: 1rem;
    font-weight: 600;
    color: #2c3e50;
  }

  @media (max-width: 768px) {
    .featured-post {
      flex-direction: column;
    }

    .featured-post-image {
      height: 250px;
    }

    .blog-posts {
      grid-template-columns: 1fr;
    }
  }
</style>

<script src="https://cdnjs.cloudflare.com/ajax/libs/animejs/3.2.1/anime.min.js"></script>
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