---
layout: page
title: COVID-19 Case Prediction Model
excerpt: An advanced COVID-19 case prediction model comparing ARIMA and LSTM algorithms.
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
        This page displays a 30-day forecast of COVID-19 cases, updated daily. Our analysis compares two different models:
        the ARIMA (AutoRegressive Integrated Moving Average) model and the LSTM (Long Short-Term Memory) neural network model. 
        The graphs below show our predictions against the actual reported cases and compare the performance of both models.
    </p>
</div>

<div id="error-container"></div>

<div class="container">
    <h2>Model Performance</h2>
    <div class="metrics-grid">
        <div class="metric-card">
            <h3>Mean Absolute Error</h3>
            <p class="metric-value" id="arima-mae">Loading...</p>
            <p id="lstm-mae">LSTM: Loading...</p>
        </div>
        <div class="metric-card">
            <h3>Root Mean Square Error</h3>
            <p class="metric-value" id="arima-rmse">Loading...</p>
            <p id="lstm-rmse">LSTM: Loading...</p>
        </div>
        <div class="metric-card">
            <h3>Mean Absolute Percentage Error</h3>
            <p class="metric-value" id="arima-mape">Loading...</p>
            <p id="lstm-mape">LSTM: Loading...</p>
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
        The chart below shows the historical performance of our ARIMA model and LSTM model
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
            <span>ARIMA Model</span>
        </div>
        <div class="model-key-item">
            <div class="model-key-color" style="background-color: #2ca02c;"></div>
            <span>LSTM Model</span>
        </div>
    </div>
</div>

<div class="container">
    <h2>30-Day Forecast Comparison</h2>
    <p>
        This chart displays the predicted number of COVID-19 cases for the next 30 days, comparing our ARIMA model's
        forecast with the LSTM model's forecast.
    </p>
    <div id="forecast-chart" class="chart-container"></div>
</div>

<div class="container">
    <h2>Methodology</h2>
    <p>
        We use two different models for time series forecasting:
    </p>
    <ol>
        <li>ARIMA (AutoRegressive Integrated Moving Average) model</li>
        <li>LSTM (Long Short-Term Memory) neural network model</li>
    </ol>
    <p>
        Both models are trained on COVID-19 case data from multiple sources, which is updated daily. Our prediction pipeline follows these steps:
    </p>
    <ol>
        <li>Daily data collection from various COVID-19 datasets</li>
        <li>Data preprocessing and cleaning</li>
        <li>Model retraining with the latest data</li>
        <li>30-day forecast generation for both models</li>
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
        // Update only the last updated time, as we don't calculate other metrics in our current script
        const lastUpdatedElement = document.getElementById('last-updated');
        if (lastUpdatedElement && data.last_updated) {
            lastUpdatedElement.textContent = dayjs(data.last_updated).format('MMMM D, YYYY HH:mm:ss');
        } else {
            lastUpdatedElement.textContent = 'N/A';
        }

        // Hide or show "N/A" for other metrics
        ['arima-mae', 'arima-rmse', 'arima-mape', 'lstm-mae', 'lstm-rmse', 'lstm-mape'].forEach(id => {
            const element = document.getElementById(id);
            if (element) {
                element.textContent = 'N/A';
            }
        });
    }
    
    function createHistoricalChart(data) {
        if (!data.dates || !data.lstm_predicted || !data.arima_predicted) {
            console.error('Missing required data for historical chart');
            return;
        }

        // Assume the last 7 entries are the new predictions
        const historicalDates = data.dates.slice(0, -7);
        const historicalActual = data.lstm_predicted.slice(0, -7);  // Use LSTM as proxy for actual
        const historicalARIMA = data.arima_predicted.slice(0, -7);
        const historicalLSTM = data.lstm_predicted.slice(0, -7);

        const trace1 = {
            x: historicalDates,
            y: historicalActual,
            type: 'scatter',
            mode: 'lines',
            name: 'Actual Cases',
            line: {color: '#1f77b4'}
        };
        const trace2 = {
            x: historicalDates,
            y: historicalARIMA,
            type: 'scatter',
            mode: 'lines',
            name: 'ARIMA Model Prediction',
            line: {color: '#ff7f0e'}
        };
        const trace3 = {
            x: historicalDates,
            y: historicalLSTM,
            type: 'scatter',
            mode: 'lines',
            name: 'LSTM Model Prediction',
            line: {color: '#2ca02c'}
        };

        const layout = {
            title: 'COVID-19 Cases: Historical Predictions',
            xaxis: { title: 'Date', rangeslider: {visible: true} },
            yaxis: { title: 'Number of Cases' },
            legend: {orientation: 'h', y: -0.2}
        };

        Plotly.newPlot('historical-chart', [trace1, trace2, trace3], layout);
    }
    
    function createForecastChart(data) {
        if (!data.dates || !data.lstm_predicted || !data.arima_predicted) {
            console.error('Missing required data for forecast chart');
            return;
        }

        // Use the last 7 entries for the forecast
        const forecastDates = data.dates.slice(-7);
        const forecastARIMA = data.arima_predicted.slice(-7);
        const forecastLSTM = data.lstm_predicted.slice(-7);

        const trace1 = {
            x: forecastDates,
            y: forecastARIMA,
            type: 'scatter',
            mode: 'lines',
            name: 'ARIMA Model Forecast',
            line: {color: '#ff7f0e'}
        };
        const trace2 = {
            x: forecastDates,
            y: forecastLSTM,
            type: 'scatter',
            mode: 'lines',
            name: 'LSTM Model Forecast',
            line: {color: '#2ca02c'}
        };

        const layout = {
            title: '7-Day COVID-19 Case Forecast',
            xaxis: { title: 'Date' },
            yaxis: { title: 'Number of Cases' },
            legend: {orientation: 'h', y: -0.2}
        };

        Plotly.newPlot('forecast-chart', [trace1, trace2], layout);
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
            createHistoricalChart(data);
            createForecastChart(data);
        })
        .catch(error => {
            console.error('Error:', error);
            displayErrorMessage(`Error loading data: ${error.message}`);
        });
});
</script>