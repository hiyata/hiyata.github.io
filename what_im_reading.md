---
layout: default
title: What I'm Reading
---

<header class="page-header">
  <div class="page-header-inner">
    <span class="kicker">Log</span>
    <h1>What I'm Reading</h1>
    <p id="current-date"></p>
  </div>
</header>

<div class="reading-list-page">
    <style>
        .reading-list-page {
            max-width: var(--content-width);
            margin: 0 auto;
            padding: clamp(2rem, 4vh, 2.75rem) max(1.5rem, 4vw) 4rem;
            color: var(--ink);
        }
        .reading-list-page h2 {
            font-family: var(--mono);
            font-size: 0.78em;
            text-transform: uppercase;
            letter-spacing: 0.06em;
            font-weight: 700;
            color: var(--ink-faint);
            margin: 0 0 1.1rem;
            text-align: left;
        }
        .container {
            display: flex;
            flex-wrap: wrap;
            gap: 1rem;
            margin-bottom: 1rem;
        }
        .feed, .recommendations {
            flex: 1 1 45%;
            min-width: 280px;
            padding: 1.25rem 1.4rem;
            border-radius: var(--radius-md);
            background: var(--surface);
            border: 1px solid var(--border);
        }
        .reading-list-page ul {
            list-style-type: none;
            padding: 0;
            margin: 0;
        }
        .reading-list-page li {
            margin-bottom: 15px;
        }
        .reading-list-page a {
            color: var(--ink);
            text-decoration: none;
            font-weight: 600;
        }
        .reading-list-page a:hover {
            color: var(--accent);
            text-decoration: underline;
        }
        .recommendations .book, .recommendations .paper {
            display: flex;
            margin-bottom: 15px;
            border-bottom: 1px solid var(--border);
            padding-bottom: 15px;
        }
        .recommendations .book:last-child, .recommendations .paper:last-child {
            border-bottom: none;
            margin-bottom: 0;
            padding-bottom: 0;
        }
        .recommendations .book img, .recommendations .paper img {
            width: 64px;
            height: 96px;
            object-fit: contain;
            margin-right: 15px;
            object-position: center top;
            background-color: var(--surface-muted);
            border: 1px solid var(--border);
            border-radius: var(--radius-sm);
        }
        .recommendations .book h3, .recommendations .paper h3 {
            margin-top: 0;
            font-size: 0.98em;
            font-weight: 700;
            color: var(--ink);
        }
        .recommendations .book p, .recommendations .paper p {
            margin: 0;
            font-size: 0.88em;
            color: var(--ink-soft);
            line-height: 1.55;
        }
        .recommendations .book .details, .recommendations .paper .details {
            flex: 1;
        }
        .recommendations .book .author, .recommendations .paper .author {
            font-family: var(--mono);
            font-size: 0.76em;
            color: var(--ink-faint);
            margin-bottom: 5px;
        }
        #arxiv-feed li, #pubmed-feed li {
            list-style: none;
            margin-bottom: 15px;
            border-bottom: 1px solid var(--border);
            padding-bottom: 10px;
            font-size: 0.9em;
            line-height: 1.55;
        }
        #arxiv-loading, #pubmed-loading {
            text-align: left;
            color: var(--ink-faint);
            font-size: 0.9em;
        }
        #arxiv-error, #pubmed-error {
            color: var(--accent);
            text-align: left;
            display: none;
        }
        .feed-updated {
            margin: 0.75rem 0 0;
            font-family: var(--mono);
            font-size: 0.72em;
            color: var(--ink-faint);
        }
    </style>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const currentDate = new Date().toLocaleDateString('en-US', {
                year: 'numeric',
                month: 'long',
                day: 'numeric'
            });
            document.getElementById('current-date').textContent = currentDate;

            // Both feeds are fetched server-side by a scheduled GitHub Action
            // (.github/workflows/update-feeds.yml) and committed as static
            // JSON, since neither pubmed.ncbi.nlm.nih.gov nor export.arxiv.org
            // send CORS headers, so a direct browser fetch from this site
            // gets blocked. Reading a same-origin JSON file sidesteps that
            // entirely, with no third-party proxy and no API key involved.
            loadFeed({
                url: '{{ "/assets/data/pubmed-feed.json" | relative_url }}',
                loadingEl: document.getElementById('pubmed-loading'),
                errorEl: document.getElementById('pubmed-error'),
                listEl: document.getElementById('pubmed-feed'),
                errorText: 'Could not load the PubMed feed right now. Please try again later.',
                renderItem: function(item) {
                    return `<a href="${item.link}" target="_blank" rel="noopener">${item.title}</a><br>` +
                        `<small>${item.date || ''}</small><br>` +
                        `<small>${item.summary || ''}</small>`;
                }
            });

            loadFeed({
                url: '{{ "/assets/data/arxiv-feed.json" | relative_url }}',
                loadingEl: document.getElementById('arxiv-loading'),
                errorEl: document.getElementById('arxiv-error'),
                listEl: document.getElementById('arxiv-feed'),
                errorText: 'Could not load the arXiv feed right now. Please try again later.',
                emptyText: 'No recent papers found related to genomic language models. This is a very specific and fairly new field, so results may be limited.',
                renderItem: function(item) {
                    const published = item.date ? new Date(item.date).toLocaleDateString() : '';
                    const authors = (item.authors || []).join(', ');
                    return `<a href="${item.link}" target="_blank" rel="noopener">${item.title}</a><br>` +
                        `<small>Authors: ${authors}</small><br>` +
                        `<small>Published: ${published}</small><br>` +
                        `<small>${item.summary || ''}</small>`;
                }
            });

            async function loadFeed(config) {
                config.loadingEl.style.display = 'block';
                config.errorEl.style.display = 'none';
                config.listEl.innerHTML = '';

                try {
                    const response = await fetch(config.url, { cache: 'no-store' });
                    if (!response.ok) throw new Error(`HTTP ${response.status}`);
                    const data = await response.json();
                    const items = data.items || [];

                    if (items.length === 0) {
                        config.listEl.innerHTML = `<li>${config.emptyText || 'No items found.'}</li>`;
                    } else {
                        const list = document.createElement('ul');
                        items.slice(0, 5).forEach(function(item) {
                            const li = document.createElement('li');
                            li.innerHTML = config.renderItem(item);
                            list.appendChild(li);
                        });
                        config.listEl.appendChild(list);
                    }

                    if (data.generated_at) {
                        const updated = document.createElement('p');
                        updated.className = 'feed-updated';
                        updated.textContent = 'Updated ' + new Date(data.generated_at).toLocaleString('en-US', {
                            dateStyle: 'medium',
                            timeStyle: 'short'
                        });
                        config.listEl.appendChild(updated);
                    }
                } catch (error) {
                    console.error('Error loading feed:', config.url, error);
                    config.errorEl.textContent = config.errorText;
                    config.errorEl.style.display = 'block';
                } finally {
                    config.loadingEl.style.display = 'none';
                }
            }
        });
    </script>

    <div class="container">
        <div class="feed">
            <h2>My PubMed Feed</h2>
            <div id="pubmed-loading">Loading PubMed articles...</div>
            <div id="pubmed-error" style="display:none;"></div>
            <div id="pubmed-feed"></div>
        </div>
        <div class="feed">
            <h2>My arXiv Feed</h2>
            <div id="arxiv-loading">Loading arXiv papers...</div>
            <div id="arxiv-error" style="display:none;"></div>
            <div id="arxiv-feed"></div>
        </div>
    </div>

    <div class="container">
        <div class="recommendations">
            <h2>Recommended Books</h2>

            <div class="book">
                <img src="{{ '/assets/images/prob_ml_intro_cover.jpg' | relative_url }}" alt="Book Cover">
                <div class="details">
                    <h3>
                        <a href="https://www.amazon.com/Probabilistic-Machine-Learning-Introduction-Computation/dp/0262046822" target="_blank">
                            Probabilistic Machine Learning: An Introduction
                        </a>
                    </h3>
                    <div class="author">Kevin P. Murphy</div>
                    <p>I cannot recommend this book enough. I will warn new readers that it is VERY heavy in statistics and mathematics. If you are just starting out, this might be a good book later down the line. </p>
                </div>
            </div>


            <div class="book">
                <img src="{{ '/assets/images/hundred-page-machine_learning_book_cover.jpg' | relative_url }}" alt="Book Cover">
                <div class="details">
                    <h3>                        
                        <a href="https://themlbook.com" target="_blank">
                            The Hundred-Page Machine Learning Book
                        </a>
                        </h3>
                    <div class="author"> Andriy Burkov</div>
                    <p></p>
                </div>
            </div>

            <!-- Add more books as needed -->

        </div>
        <div class="recommendations">
            <h2>Recommended Papers</h2>

        <div class="paper">
            <img src="{{ '/assets/images/DNABERT.png' | relative_url }}" alt="DNABERT">
            <div class="details">
                <h3><a href="https://academic.oup.com/bioinformatics/article/37/15/2112/6128680" target="_blank">DNABERT</a></h3>
                <div class="author">Yanrong Ji, Zhihan Zhou, Han Liu, Ramana V Davuluri.</div>
                <p>Published in 2021, this is the first foundational model trained on DNA sequences. DNABERT is a 110-million parameter model trained on DNA k-mers.</p>
            </div>
        </div>


            <div class="paper">
                <img src="{{ '/assets/images/Toward_a_theory_of_evolution_as_multilevel_learning.png' | relative_url }}" alt="Multi-level_learning">
                <div class="details">
                    <h3>Toward a Theory of Evolution as Multilevel Learning</h3>
                    <div class="author">Vanchurin V, Wolf YI, Katsnelson MI, Koonin EV.</div>
                    <p></p>
                </div>
            </div>

            <!-- Add more papers as needed -->
        </div>
    </div>
</div>
