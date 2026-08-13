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
    </style>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-rss/3.3.0/jquery.rss.min.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const currentDate = new Date().toLocaleDateString('en-US', {
                year: 'numeric',
                month: 'long',
                day: 'numeric'
            });
            document.getElementById('current-date').textContent = currentDate;

            // PubMed feed
            $("#pubmed-feed").rss("https://pubmed.ncbi.nlm.nih.gov/rss/search/1xCFUMSbAMYitB6LKyB5opiesUFp1inW-kMm4Ly8hr-nJYagWd/?limit=15&utm_campaign=pubmed-2&fc=20240820105625", {
                limit: 5,
                effect: 'slideFastSynced',
                layoutTemplate: "<ul>{entries}</ul>",
                entryTemplate: '<li><a href="{url}">{title}</a><br/><small>{date}</small><br/>{shortBodyPlain}</li>',
                error: function() {
                    document.getElementById('pubmed-loading').style.display = 'none';
                    document.getElementById('pubmed-error').style.display = 'block';
                    document.getElementById('pubmed-error').textContent = 'Error loading PubMed feed. Please try again later.';
                },
                success: function() {
                    document.getElementById('pubmed-loading').style.display = 'none';
                }
            });

            // Function to fetch and display most recent arXiv papers related to genomic LLM
            async function fetchArxivPapers() {
                const loadingElement = document.getElementById('arxiv-loading');
                const errorElement = document.getElementById('arxiv-error');
                const arxivFeed = document.getElementById('arxiv-feed');

                loadingElement.style.display = 'block';
                errorElement.style.display = 'none';
                arxivFeed.innerHTML = '';

                // Updated query to focus on genomic LLM
                const query = encodeURIComponent('all:("genomic language model" OR "genomic LLM" OR "genomics LLM" OR "genomics language model" OR (genomic AND "large language model"))');
                const url = `https://export.arxiv.org/api/query?search_query=${query}&sortBy=lastUpdatedDate&sortOrder=descending&start=0&max_results=5`;

                try {
                    const response = await fetch(url);
                    const xmlText = await response.text();
                    const parser = new DOMParser();
                    const xmlDoc = parser.parseFromString(xmlText, "text/xml");

                    const entries = xmlDoc.getElementsByTagName('entry');

                    console.log(`Found ${entries.length} entries related to genomic LLM`);

                    if (entries.length === 0) {
                        arxivFeed.innerHTML = '<li>No recent papers found related to genomic language models. This is a very specific and potentially new field, so results may be limited.</li>';
                    } else {
                        for (let i = 0; i < Math.min(entries.length, 5); i++) { // Limit to top 5 results
                            const entry = entries[i];
                            const title = entry.getElementsByTagName('title')[0].textContent;
                            const authors = Array.from(entry.getElementsByTagName('author')).map(author => author.getElementsByTagName('name')[0].textContent).join(', ');
                            const link = entry.getElementsByTagName('id')[0].textContent;
                            const published = new Date(entry.getElementsByTagName('published')[0].textContent);
                            const summary = entry.getElementsByTagName('summary')[0].textContent.slice(0, 200) + '...';

                            const listItem = document.createElement('li');
                            listItem.innerHTML = `
                                <a href="${link}" target="_blank">${title}</a><br>
                                <small>Authors: ${authors}</small><br>
                                <small>Published: ${published.toLocaleDateString()}</small><br>
                                <small>${summary}</small>
                            `;
                            arxivFeed.appendChild(listItem);
                        }
                    }
                } catch (error) {
                    console.error('Error fetching arXiv papers:', error);
                    errorElement.textContent = 'Error fetching arXiv papers. Please try again later.';
                    errorElement.style.display = 'block';
                } finally {
                    loadingElement.style.display = 'none';
                }
            }

            // Call the function to fetch arXiv papers
            fetchArxivPapers();
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
