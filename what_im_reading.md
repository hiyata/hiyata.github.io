---
layout: default
title: My Reading List
---

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Reading List</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    <style>
        body {
            font-family: 'Helvetica Neue', Arial, sans-serif;
            background-color: #f3f4f6;
            margin: 0;
            padding: 20px;
            color: #333;
        }
        h1 {
            font-size: 2.5em;
            text-align: center;
            color: #2c3e50;
            margin-bottom: 10px;
            letter-spacing: 1px;
        }
        .subheader {
            font-size: 1.2em;
            text-align: center;
            color: #7f8c8d;
            margin-bottom: 30px;
        }
        .container {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
        }
        .feed, .recommendations {
            flex: 1 1 45%;
            background-color: #ffffff;
            padding: 20px;
            margin: 10px;
            border-radius: 8px;
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
            transition: transform 0.2s ease;
        }
        .feed:hover, .recommendations:hover {
            transform: translateY(-5px);
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
        }
        h2 {
            font-size: 1.8em;
            color: #34495e;
            margin-bottom: 15px;
            border-bottom: 2px solid #bdc3c7;
            padding-bottom: 5px;
            text-align: center;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            margin-bottom: 15px;
        }
        a {
            color: #2980b9;
            text-decoration: none;
            font-weight: bold;
        }
        a:hover {
            text-decoration: underline;
        }
        .recommendations .book, .recommendations .paper {
            display: flex;
            margin-bottom: 20px;
            border-bottom: 1px solid #bdc3c7;
            padding-bottom: 15px;
        }
        .recommendations .book img, .recommendations .paper img {
            width: 100px;
            height: 150px;
            object-fit: contain;
            border-radius: 5px;
            margin-right: 15px;
            object-position: center;
            background-color: #f3f4f6;
        }
        .recommendations .book h3, .recommendations .paper h3 {
            margin-top: 0;
            font-size: 1.4em;
            color: #2c3e50;
        }
        .recommendations .book p, .recommendations .paper p {
            margin: 0;
            font-size: 0.95em;
            color: #7f8c8d;
        }
        .recommendations .book .details, .recommendations .paper .details {
            flex: 1;
        }
        .recommendations .book .author, .recommendations .paper .author {
            font-weight: bold;
            margin-bottom: 5px;
        }
        #arxiv-feed li, #pubmed-feed li {
            list-style: none;
            margin-bottom: 20px;
            border-bottom: 1px solid #ecf0f1;
            padding-bottom: 10px;
        }
        #arxiv-loading, #pubmed-loading {
            text-align: center;
            color: #7f8c8d;
        }
        #arxiv-error, #pubmed-error {
            color: #e74c3c;
            text-align: center;
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
</head>
<body>
    <h1>My Reading List</h1>
    <div class="subheader" id="current-date"></div>

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
                <img src="assets/images/prob_ml_intro_cover.jpg" alt="Book Cover">
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
                <img src="assets/images/hundred-page-machine_learning_book_cover.jpg" alt="Book Cover">
                <div class="details">
                    <h3>                        
                        <a href="https://themlbook.com" target="_blank">
                            The Hundred-Page Machine Learning Book
                        </a>
                        </h3>
                    <div class="author"> Andriy Burkov</div>
                    <p>A brief review or description of why this book is recommended. This section allows you to highlight key takeaways or insights that make this book valuable.</p>
                </div>
            </div>

            <!-- Add more books as needed -->

        </div>
        <div class="recommendations">
            <h2>Recommended Papers</h2>

            <div class="paper">
                <img src="path_to_paper_thumbnail.jpg" alt="Paper Thumbnail">
                <div class="details">
                    <h3>Title of the Paper</h3>
                    <div class="author">Paper Author</div>
                    <p>A brief review or description of the paper, focusing on its contributions and why it’s worth reading.</p>
                </div>
            </div>

            <div class="paper">
                <img src="path_to_another_paper_thumbnail.jpg" alt="Paper Thumbnail">
                <div class="details">
                    <h3>Title of Another Paper</h3>
                    <div class="author">Another Paper Author</div>
                    <p>A brief review or description of the paper, focusing on its contributions and why it’s worth reading.</p>
                </div>
            </div>

            <!-- Add more papers as needed -->
        </div>
    </div>
</body>
</html>
