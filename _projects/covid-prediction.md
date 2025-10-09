---
layout: page
title: COVID-19 Case Prediction Model Comparison
excerpt: A COVID-19 case prediction model comparing LSTM/GRU, ARIMA, Random Forest, and XGBoost algorithms.
category: virology
permalink: /covid-prediction/
---
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>COVID-19 Case Prediction Model Comparison</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js" defer></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/dayjs/1.10.4/dayjs.min.js" defer></script>
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
        h1, h2, h3 {
            color: #2c3e50;
        }
        .container {
            background-color: #fff;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .alert {
            background-color: #f8d7da;
            border-color: #f5c6cb;
            color: #721c24;
            padding: 15px;
            border-radius: 4px;
            margin-bottom: 20px;
        }
        .performance-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }
        .performance-card {
            background-color: #f8f9fa;
            border-radius: 8px;
            padding: 20px;
            text-align: center;
            transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
        }
        .performance-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        .performance-card h3 {
            margin-top: 0;
            color: #34495e;
            font-size: 1.2em;
        }
        .performance-value {
            font-size: 2em;
            font-weight: bold;
            color: #2980b9;
            margin: 10px 0;
        }
        .performance-label {
            font-size: 0.9em;
            color: #7f8c8d;
        }
        .last-updated {
            text-align: center;
            margin-top: 20px;
            font-style: italic;
            color: #7f8c8d;
        }
        .chart-container {
            height: 500px;
            margin-top: 20px;
        }
        .model-key {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            margin-top: 20px;
        }
        .model-key-item {
            margin: 5px 10px;
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
</head>
<body>
    <div class="container">
        <h1>COVID-19 Case Prediction Model Comparison</h1>
        <div class="alert">
            <strong>Important Notice:</strong> Due to the discontinuation of daily COVID-19 case reporting to the WHO, our daily predictions have been discontinued. The information below represents our last available data and predictions.
        </div>
        <p>
            This page displays a 7-day comparison of COVID-19 case predictions using four different models:
            LSTM/GRU (Long Short-Term Memory/Gated Recurrent Unit), ARIMA (AutoRegressive Integrated Moving Average),
            Random Forest, and XGBoost. The graphs below show our predictions against the actual reported cases
            and compare the performance of all models.
        </p>
    </div>

    <div id="error-container"></div>

    <div class="container">
        <h2>Model Performance</h2>
        <p>The performance of each model is measured using the Mean Absolute Percentage Error (MAPE). Lower values indicate better performance.</p>
        <div class="performance-grid">
            <div class="performance-card">
                <h3>LSTM/GRU</h3>
                <div class="performance-value" id="lstm-gru-mape">Loading...</div>
                <div class="performance-label">MAPE</div>
            </div>
            <div class="performance-card">
                <h3>ARIMA</h3>
                <div class="performance-value" id="arima-mape">Loading...</div>
                <div class="performance-label">MAPE</div>
            </div>
            <div class="performance-card">
                <h3>Random Forest</h3>
                <div class="performance-value" id="rf-mape">Loading...</div>
                <div class="performance-label">MAPE</div>
            </div>
            <div class="performance-card">
                <h3>XGBoost</h3>
                <div class="performance-value" id="xgb-mape">Loading...</div>
                <div class="performance-label">MAPE</div>
            </div>
        </div>
        <div class="last-updated">
            Last Updated: <span id="last-updated">Loading...</span>
        </div>
    </div>

    <div class="container">
        <h2>7-Day Model Comparison</h2>
        <p>
            This chart displays the actual cases and predicted number of COVID-19 cases for the last 7 days,
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
            We used four different models for time series forecasting:
        </p>
        <ol>
            <li>LSTM/GRU (Long Short-Term Memory/Gated Recurrent Unit) neural network model</li>
            <li>ARIMA (AutoRegressive Integrated Moving Average) model</li>
            <li>Random Forest Regressor</li>
            <li>XGBoost Regressor</li>
        </ol>
        <p>
            All models were trained on COVID-19 case data from the WHO dataset. Our prediction pipeline followed these steps:
        </p>
        <ol>
            <li>Daily data collection from the WHO COVID-19 dataset</li>
            <li>Data preprocessing and cleaning</li>
            <li>Feature creation with a sequence length of 90 days</li>
            <li>Model training with the latest data</li>
            <li>7-day hindcast generation for all models</li>
            <li>Comparison of predictions with actual reported cases</li>
            <li>Calculation of Mean Absolute Percentage Error (MAPE) for each model</li>
        </ol>
        <p>
            For more details on our methodology, please visit our <a href="https://github.com/hiyata/covid-19-predictor">GitHub repository</a>.
        </p>
    </div>

<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/dayjs/1.10.4/dayjs.min.js"></script>
<script>
document.addEventListener('DOMContentLoaded', function() {
    function displayErrorMessage(message) {
        const errorContainer = document.getElementById('error-container');
        errorContainer.innerHTML = `<div class="error-message">${message}</div>`;
    }
    
    function updateMetrics(data) {
        document.getElementById('lstm-gru-mape').textContent = data.mape.lstm_gru.toFixed(2) + '%';
        document.getElementById('arima-mape').textContent = data.mape.arima.toFixed(2) + '%';
        document.getElementById('rf-mape').textContent = data.mape.random_forest.toFixed(2) + '%';
        document.getElementById('xgb-mape').textContent = data.mape.xgboost.toFixed(2) + '%';
        document.getElementById('last-updated').textContent = dayjs(data.last_updated).format('MMMM D, YYYY HH:mm:ss');
    }
    
    function createComparisonChart(data) {
        if (typeof Plotly === 'undefined') {
            displayErrorMessage('Plotly library is not loaded, please refresh the page to fix this.');
            return;
        }

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
            y: data.lstm_gru_predictions,
            type: 'scatter',
            mode: 'lines+markers',
            name: 'LSTM/GRU Prediction',
            line: {color: '#1f77b4'}
        };
        
        const arimaTrace = {
            x: data.dates,
            y: data.arima_predictions,
            type: 'scatter',
            mode: 'lines+markers',
            name: 'ARIMA Prediction',
            line: {color: '#ff7f0e'}
        };
        
        const rfTrace = {
            x: data.dates,
            y: data.rf_predictions,
            type: 'scatter',
            mode: 'lines+markers',
            name: 'Random Forest Prediction',
            line: {color: '#2ca02c'}
        };
        
        const xgbTrace = {
            x: data.dates,
            y: data.xgb_predictions,
            type: 'scatter',
            mode: 'lines+markers',
            name: 'XGBoost Prediction',
            line: {color: '#d62728'}
        };

        const layout = {
            title: '7-Day COVID-19 Case Prediction Comparison',
            xaxis: { title: 'Date' },
            yaxis: { title: 'Number of Cases' },
            legend: {orientation: 'h', y: -0.2}
        };

        Plotly.newPlot('comparison-chart', [actualTrace, lstmGruTrace, arimaTrace, rfTrace, xgbTrace], layout);
    }

    function fetchData() {
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
    }

    if (typeof Plotly === 'undefined') {
        const plotlyScript = document.createElement('script');
        plotlyScript.src = 'https://cdn.plot.ly/plotly-latest.min.js';
        plotlyScript.onload = fetchData;
        plotlyScript.onerror = function() {
            displayErrorMessage('Failed to load Plotly library, please refresh the page to fix this.');
        };
        document.head.appendChild(plotlyScript);
    } else {
        fetchData();
    }
});
</script>
</body>
</html>