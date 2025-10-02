---
layout: default
category: virology
excerpt: Interactive tool for virus host prediction using deep learning
title: Virus Host Classifier
---

<link rel="stylesheet" href="{{ site.baseurl }}/assets/css/virus-classifier.css">

# Virus Host Classifier

## Upload your sequence for analysis
This tool uses deep learning to predict whether a virus sequence is likely to infect human or non-human hosts. Simply upload your FASTA file to get predictions and confidence scores.

<div class="virus-classifier">
    <div class="upload-section">
        <div class="file-input-wrapper">
            <input type="file" id="fastaFile" accept=".fasta,.fa,.txt" class="file-input" />
            <label for="fastaFile">Choose FASTA File</label>
        </div>
        <button id="analyzeButton" class="analyze-button" disabled>Analyze Sequence</button>
    </div>
    
    <div id="results" class="results-section" style="display: none;">
        <h3>Prediction Results</h3>
        <div id="predictionOutput"></div>
    </div>
    
    <div id="loading" class="loading-section" style="display: none;">
        <div class="loading-spinner"></div>
        <p>Analyzing sequence...</p>
    </div>

    <div class="info-section">
        <h3>About this classifier</h3>
        <p>This deep learning model analyzes viral genomic sequences using k-mer frequencies to predict potential host organisms. The model provides:</p>
        <ul>
            <li>Binary classification (human vs non-human host)</li>
            <li>Confidence scores for predictions</li>
            <li>Most influential sequence patterns (k-mers)</li>
        </ul>
        <p>Note: This is a research tool and predictions should be validated with additional evidence.</p>
    </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/@gradio/client@2.3.0/dist/gradio.umd.min.js"></script>
<script src="{{ site.baseurl }}/assets/js/virus-classifier.js"></script>