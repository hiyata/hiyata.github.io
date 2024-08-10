---
layout: page
title: COVID-19 Case Prediction Model
excerpt: An advanced COVID-19 case prediction model comparing hybrid deep learning, Prophet, and ARIMA algorithms.
permalink: /covid-prediction/
category: virology
---

<style>
    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        color: #333;
        max-width: 1200px;
        margin: 0 auto;
        padding: 20px;
        background-color: #f4f4f4;
    }
    h1, h2 {
        color: #2c3e50;
    }
    .container {
        background-color: #fff;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .metrics-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 20px;
        margin-top: 20px;
    }
    .metric-card {
        background-color: #f8f9fa;
        border-radius: 8px;
        padding: 15px;
        text-align: center;
    }
    .metric-card h3 {
        margin-top: 0;
        color: #34495e;
    }
    .metric-value {
        font-size: 24px;
        font-weight: bold;
        color: #2980b9;
    }
    .chart-container {
        height: 500px;
        margin-top: 20px;
    }
    .model-key {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }
    .model-key-item {
        margin: 0 10px;
        display: flex;
        align-items: center;
    }
    .model-key-color {
        width: 20px;
        height: 20px;
        margin-right: 5px;
        border-radius: 50%;
    }
    .error-message {
        color: #e74c3c;
        font-weight: bold;
        text-align: center;
        padding: 20px;
        background-color: #fadbd8;
        border-radius: 8px;
        margin-top: 20px;
    }
</style>

<div class="container">
    <h1>COVID-19 Case Prediction Model</h1>
    <p>
        This page displays a 30-day forecast of COVID-19 cases, updated daily. Our analysis compares three different models:
        a hybrid deep learning approach (CNN-LSTM-GRU), Facebook's Prophet model, and the ARIMA model. The graphs below show
        our predictions against the actual reported cases and compare the performance of all three models.
    </p>
</div>

<div id="error-container"></div>

<div class="container">
    <h2>Model Performance</h2>
    <div class="metrics-grid">
        <div class="metric-card">
            <h3>Mean Absolute Error</h3>
            <p class="metric-value" id="hybrid-mae">Loading...</p>
            <p id="prophet-mae">Prophet: Loading...</p>
            <p id="arima-mae">ARIMA: Loading...</p>
        </div>
        <div class="metric-card">
            <h3>Root Mean Square Error</h3>
            <p class="metric-value" id="hybrid-rmse">Loading...</p>
            <p id="prophet-rmse">Prophet: Loading...</p>
            <p id="arima-rmse">ARIMA: Loading...</p>
        </div>
        <div class="metric-card">
            <h3>Mean Absolute Percentage Error</h3>
            <p class="metric-value" id="hybrid-mape">Loading...</p>
            <p id="prophet-mape">Prophet: Loading...</p>
            <p id="arima-mape">ARIMA: Loading...</p>
        </div>
        <div class="metric-card">
            <h3>Last Updated</h3>
            <p class="metric-value" id="last-updated">Loading...</p>
        </div>
    </div>
</div>

<div class="container">
    <h2>Historical Performance</h2>
    <p>
        The chart below shows the historical performance of our hybrid model, the Prophet model, and the ARIMA model
        compared to the actual reported cases.
    </p>
    <div id="historical-chart" class="chart-container"></div>
    <div class="model-key">
        <div class="model-key-item">
            <div class="model-key-color" style="background-color: #1f77b4;"></div>
            <span>Actual Cases</span>
        </div>
        <div class="model-key-item">
            <div class="model-key-color" style="background-color: #ff7f0e;"></div>
            <span>Hybrid Model</span>
        </div>
        <div class="model-key-item">
            <div class="model-key-color" style="background-color: #2ca02c;"></div>
            <span>Prophet Model</span>
        </div>
        <div class="model-key-item">
            <div class="model-key-color" style="background-color: #d62728;"></div>
            <span>ARIMA Model</span>
        </div>
    </div>
</div>

<div class="container">
    <h2>30-Day Forecast Comparison</h2>
    <p>
        This chart displays the predicted number of COVID-19 cases for the next 30 days, comparing our hybrid model's
        forecast with the Prophet model's forecast and the ARIMA model's forecast.
    </p>
    <div id="forecast-chart" class="chart-container"></div>
</div>

<div class="container">
    <h2>Methodology</h2>
    <p>
        We use three different models for time series forecasting:
    </p>
    <ol>
        <li>A hybrid model combining CNN, LSTM, and GRU layers</li>
        <li>Facebook's Prophet model</li>
        <li>ARIMA (AutoRegressive Integrated Moving Average) model</li>
    </ol>
    <p>
        All models are trained on COVID-19 case data from multiple sources, which is updated daily. Our prediction pipeline follows these steps:
    </p>
    <ol>
        <li>Daily data collection from various COVID-19 datasets</li>
        <li>Data preprocessing and cleaning</li>
        <li>Model retraining with the latest data</li>
        <li>30-day forecast generation for all three models</li>
        <li>Daily comparison of predictions with actual reported cases</li>
    </ol>
    <p>
        For more details on our methodology, please visit our <a href="https://github.com/hiyata/covid-19-predictor">GitHub repository</a>.
    </p>
</div>

<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/dayjs/1.10.4/dayjs.min.js"></script>
<script>
document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM content loaded');
    
    function displayErrorMessage(message) {
        const errorContainer = document.getElementById('error-container');
        errorContainer.innerHTML = `<div class="error-message">${message}</div>`;
    }
    
    function updateMetrics(data) {
        document.getElementById('hybrid-mae').textContent = data.hybrid_mae.toFixed(2);
        document.getElementById('hybrid-rmse').textContent = data.hybrid_rmse.toFixed(2);
        document.getElementById('hybrid-mape').textContent = data.hybrid_mape.toFixed(2) + '%';
        document.getElementById('prophet-mae').textContent = 'Prophet: ' + data.prophet_mae.toFixed(2);
        document.getElementById('prophet-rmse').textContent = 'Prophet: ' + data.prophet_rmse.toFixed(2);
        document.getElementById('prophet-mape').textContent = 'Prophet: ' + data.prophet_mape.toFixed(2) + '%';
        document.getElementById('arima-mae').textContent = 'ARIMA: ' + data.arima_mae.toFixed(2);
        document.getElementById('arima-rmse').textContent = 'ARIMA: ' + data.arima_rmse.