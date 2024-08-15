---
layout: page
title: COVID-19 Case Prediction Model
excerpt: An advanced COVID-19 case prediction model using a hybrid CNN-LSTM-GRU approach.
category: virology
permalink: /covid-prediction/
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
        This page displays a 14-day forecast of COVID-19 cases, updated daily. Our analysis uses a hybrid model
        combining Convolutional Neural Networks (CNN), Long Short-Term Memory (LSTM), and Gated Recurrent Units (GRU).
        The graph below shows our predictions against the actual reported cases for the past 7 days and forecast for the next 7 days.
    </p>
</div>

<div id="error-container"></div>

<div class="container">
    <h2>Model Performance</h2>
    <div class="metrics-grid">
        <div class="metric-card">
            <h3>Mean Absolute Error</h3>
            <p class="metric-value" id="mae">Loading...</p>
        </div>
        <div class="metric-card">
            <h3>Root Mean Square Error</h3>
            <p class="metric-value" id="rmse">Loading...</p>
        </div>
        <div class="metric-card">
            <h3>Mean Absolute Percentage Error</h3>
            <p class="metric-value" id="mape">Loading...</p>
        </div>
        <div class="metric-card">
            <h3>Last Updated</h3>
            <p class="metric-value" id="last-updated">Loading...</p>
        </div>
    </div>
</div>

<div class="container">
    <h2>14-Day Comparison and Forecast</h2>
    <p>
        This chart displays the actual cases for the past 7 days and the predicted number of COVID-19 cases
        for the next 7 days using our hybrid model.
    </p>
    <div id="forecast-chart" class="chart-container"></div>
    <div class="model-key">
        <div class="model-key-item">
            <div class="model-key-color" style="background-color: #1f77b4;"></div>
            <span>Actual Cases</span>
        </div>
        <div class="model-key-item">
            <div class="model-key-color" style="background-color: #ff7f0e;"></div>
            <span>Predicted Cases</span>
        </div>
    </div>
</div>

<div class="container">
    <h2>Methodology</h2>
    <p>
        We use a hybrid model for time series forecasting that combines:
    </p>
    <ol>
        <li>Convolutional Neural Networks (CNN)</li>
        <li>Long Short-Term Memory (LSTM) neural networks</li>
        <li>Gated Recurrent Units (GRU)</li>
    </ol>
    <p>
        Our prediction pipeline follows these steps:
    </p>
    <ol>
        <li>Daily data collection from WHO COVID-19 dataset</li>
        <li>Data preprocessing and cleaning</li>
        <li>Model retraining with the latest data</li>
        <li>14-day forecast generation (7 days comparison + 7 days future)</li>
        <li>Daily comparison of predictions with actual reported cases</li>
    </ol>
    <p>
        For more details on our methodology, please visit our <a href="https://github.com/yourusername/covid-19-predictor">GitHub repository</a>.
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
        document.getElementById('mae').textContent = data.mae.toFixed(2);
        document.getElementById('rmse').textContent = data.rmse.toFixed(2);
        document.getElementById('mape').textContent = data.mape.toFixed(2) + '%';
        document.getElementById('last-updated').textContent = dayjs(data.last_updated).format('MMMM D, YYYY HH:mm:ss');
    }
    
    function createForecastChart(data) {
        const actualTrace = {
            x: data.comparison_dates.slice(0, 7),
            y: data.comparison_actual.slice(0, 7),
            type: 'scatter',
            mode: 'lines',
            name: 'Actual Cases',
            line: {color: '#1f77b4'}
        };
        
        const predictedTrace = {
            x: data.comparison_dates,
            y: data.comparison_predicted,
            type: 'scatter',
            mode: 'lines',
            name: 'Predicted Cases',
            line: {color: '#ff7f0e'}
        };

        const layout = {
            title: '14-Day COVID-19 Case Comparison and Forecast',
            xaxis: { title: 'Date' },
            yaxis: { title: 'Number of Cases' },
            legend: {orientation: 'h', y: -0.2}
        };

        Plotly.newPlot('forecast-chart', [actualTrace, predictedTrace], layout);
    }

    // Fetch the latest prediction data
    fetch('/assets/covid-19-files/covid_predictions.json')
        .then(response => {
            console.log('Response status:', response.status);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log('Prediction data received:', data);
            updateMetrics(data);
            createForecastChart(data);
        })
        .catch(error => {
            console.error('Error:', error);
            displayErrorMessage(`Error loading data: ${error.message}`);
        });
});
</script>