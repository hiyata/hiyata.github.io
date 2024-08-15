---
layout: page
title: COVID-19 Case Prediction Model Comparison
excerpt: An advanced COVID-19 case prediction model comparing LSTM/GRU, ARIMA, Random Forest, and XGBoost algorithms.
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
    <h1>COVID-19 Case Prediction Model Comparison</h1>
    <p>
        This page displays a 7-week forecast of COVID-19 cases, updated weekly. Our analysis compares four different models:
        LSTM/GRU (Long Short-Term Memory/Gated Recurrent Unit), ARIMA (AutoRegressive Integrated Moving Average),
        Random Forest, and XGBoost. The graph below shows our predictions against the actual reported cases
        and compares the performance of all models.
    </p>
</div>

<div id="error-container"></div>

<div class="container">
    <h2>Model Performance</h2>
    <div class="metrics-grid">
        <div class="metric-card">
            <h3>LSTM/GRU MAPE</h3>
            <p class="metric-value" id="lstm-gru-mape">Loading...</p>
        </div>
        <div class="metric-card">
            <h3>ARIMA MAPE</h3>
            <p class="metric-value" id="arima-mape">Loading...</p>
        </div>
        <div class="metric-card">
            <h3>Random Forest MAPE</h3>
            <p class="metric-value" id="rf-mape">Loading...</p>
        </div>
        <div class="metric-card">
            <h3>XGBoost MAPE</h3>
            <p class="metric-value" id="xgb-mape">Loading...</p>
        </div>
        <div class="metric-card">
            <h3>Last Updated</h3>
            <p class="metric-value" id="last-updated">Loading...</p>
        </div>
    </div>
</div>

<div class="container">
    <h2>7-Week Model Comparison</h2>
    <p>
        This chart displays the actual cases and predicted number of COVID-19 cases for the next 7 weeks,
        comparing all four models: LSTM/GRU, ARIMA, Random Forest, and XGBoost.
    </p>
    <div id="comparison-chart" class="chart-container"></div>
    <div class="model-key">
        <div class="model-key-item">
            <div class="model-key-color" style="background-color: #000000;"></div>
            <span>Actual Cases</span>
        </div>
        <div class="model-key-item">
            <div class="model-key-color" style="background-color: #1f77b4;"></div>
            <span>LSTM/GRU Model</span>
        </div>
        <div class="model-key-item">
            <div class="model-key-color" style="background-color: #ff7f0e;"></div>
            <span>ARIMA Model</span>
        </div>
        <div class="model-key-item">
            <div class="model-key-color" style="background-color: #2ca02c;"></div>
            <span>Random Forest Model</span>
        </div>
        <div class="model-key-item">
            <div class="model-key-color" style="background-color: #d62728;"></div>
            <span>XGBoost Model</span>
        </div>
    </div>
</div>

<div class="container">
    <h2>Methodology</h2>
    <p>
        We use four different models for time series forecasting:
    </p>
    <ol>
        <li>LSTM/GRU (Long Short-Term Memory/Gated Recurrent Unit) neural network model</li>
        <li>ARIMA (AutoRegressive Integrated Moving Average) model</li>
        <li>Random Forest Regressor</li>
        <li>XGBoost Regressor</li>
    </ol>
    <p>
        All models are trained on COVID-19 case data from the WHO dataset, which is updated weekly. Our prediction pipeline follows these steps:
    </p>
    <ol>
        <li>Weekly data collection from the WHO COVID-19 dataset</li>
        <li>Data preprocessing and cleaning, including log transformation and scaling</li>
        <li>Feature creation with a sequence length of 90 days</li>
        <li>Model training with the latest data</li>
        <li>7-week forecast generation for all models</li>
        <li>Comparison of predictions with actual reported cases</li>
        <li>Calculation of Mean Absolute Percentage Error (MAPE) for each model</li>
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
        document.getElementById('lstm-gru-mape').textContent = data.lstm_gru_mape.toFixed(2) + '%';
        document.getElementById('arima-mape').textContent = data.arima_mape.toFixed(2) + '%';
        document.getElementById('rf-mape').textContent = data.rf_mape.toFixed(2) + '%';
        document.getElementById('xgb-mape').textContent = data.xgb_mape.toFixed(2) + '%';
        document.getElementById('last-updated').textContent = dayjs(data.last_updated).format('MMMM D, YYYY HH:mm:ss');
    }
    
    function createComparisonChart(data) {
        const actualTrace = {
            x: data.dates,
            y: data.actual,
            type: 'scatter',
            mode: 'lines+markers',
            name: 'Actual Cases',
            line: {color: '#000000', width: 3}
        };
        
        const lstmGruTrace = {
            x: data.dates,
            y: data.lstm_gru_predicted,
            type: 'scatter',
            mode: 'lines+markers',
            name: 'LSTM/GRU Prediction',
            line: {color: '#1f77b4'}
        };
        
        const arimaTrace = {
            x: data.dates,
            y: data.arima_predicted,
            type: 'scatter',
            mode: 'lines+markers',
            name: 'ARIMA Prediction',
            line: {color: '#ff7f0e'}
        };
        
        const rfTrace = {
            x: data.dates,
            y: data.rf_predicted,
            type: 'scatter',
            mode: 'lines+markers',
            name: 'Random Forest Prediction',
            line: {color: '#2ca02c'}
        };
        
        const xgbTrace = {
            x: data.dates,
            y: data.xgb_predicted,
            type: 'scatter',
            mode: 'lines+markers',
            name: 'XGBoost Prediction',
            line: {color: '#d62728'}
        };

        const layout = {
            title: '7-Week COVID-19 Case Prediction Comparison',
            xaxis: { title: 'Date' },
            yaxis: { title: 'Number of Cases' },
            legend: {orientation: 'h', y: -0.2}
        };

        Plotly.newPlot('comparison-chart', [actualTrace, lstmGruTrace, arimaTrace, rfTrace, xgbTrace], layout);
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
            createComparisonChart(data);
        })
        .catch(error => {
            console.error('Error:', error);
            displayErrorMessage(`Error loading data: ${error.message}`);
        });
});
</script>