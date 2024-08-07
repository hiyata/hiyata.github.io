---
layout: page
title: COVID-19 Case Prediction Model
excerpt: This is a brief summary of the project.
permalink: /covid-prediction/
---

# COVID-19 Case Prediction Model

This page displays a 30-day forecast of COVID-19 cases, updated daily. Our model is trained on historical data and makes predictions for the next month. The graph below shows our predictions against the actual reported cases.

<div id="prediction-chart" style="height: 500px;"></div>

## Model Performance

<div id="performance-metrics" style="display: flex; justify-content: space-around; margin-top: 20px;">
    <div style="text-align: center; background: #f2f2f2; padding: 20px; border-radius: 10px; width: 200px;">
        <h3>Mean Absolute Error</h3>
        <p id="mae" style="font-size: 24px; font-weight: bold;">N/A</p>
    </div>
    <div style="text-align: center; background: #f2f2f2; padding: 20px; border-radius: 10px; width: 200px;">
        <h3>Root Mean Square Error</h3>
        <p id="rmse" style="font-size: 24px; font-weight: bold;">N/A</p>
    </div>
    <div style="text-align: center; background: #f2f2f2; padding: 20px; border-radius: 10px; width: 200px;">
        <h3>Mean Absolute Percentage Error</h3>
        <p id="mape" style="font-size: 24px; font-weight: bold;">N/A</p>
    </div>
    <div style="text-align: center; background: #f2f2f2; padding: 20px; border-radius: 10px; width: 200px;">
        <h3>Last Updated</h3>
        <p id="last-updated" style="font-size: 24px; font-weight: bold;">N/A</p>
    </div>
</div>

## 30-Day Forecast

The chart below shows the predicted number of COVID-19 cases for the next 30 days.

<div id="forecast-chart" style="height: 500px; margin-top: 20px;"></div>

## Methodology

We use a hybrid model combining LSTM, GRU, and CNN layers for time series forecasting. The model is trained on COVID-19 case data from multiple sources, which is updated daily. Our prediction pipeline follows these steps:

1. Daily data collection from various COVID-19 datasets
2. Model retraining with the latest 6 months of data
3. 30-day forecast generation
4. Daily comparison of predictions with actual reported cases

For more details on our methodology, please visit our [GitHub repository](https://github.com/hiyata/covid-19-predictor).

<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/dayjs/1.10.4/dayjs.min.js"></script>
<script>
document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM content loaded');
    // Fetch the latest prediction data
    fetch('/assets/covid-19-files/covid_predictions.json')
        .then(response => {
            console.log('Response status:', response.status);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();  // Get the response as JSON
        })
        .then(data => {
            console.log('Data received:', data);     
            if (!data || !Array.isArray(data.dates) || !Array.isArray(data.actual) || !Array.isArray(data.predicted)) {
                throw new Error('Data is missing required fields or they are not arrays');
            }            
            // Create the prediction chart
            const trace1 = {
                x: data.dates.slice(0, -30),
                y: data.actual.slice(0, -30),
                type: 'scatter',
                mode: 'lines',
                name: 'Actual Cases'
            };
            const trace2 = {
                x: data.dates.slice(0, -30),
                y: data.predicted.slice(0, -30),
                type: 'scatter',
                mode: 'lines',
                name: 'Predicted Cases'
            };
            const layout = {
                title: 'COVID-19 Cases: Actual vs Predicted',
                xaxis: { title: 'Date' },
                yaxis: { title: 'Number of Cases' }
            };
            Plotly.newPlot('prediction-chart', [trace1, trace2], layout);
            // Create the forecast chart
            const forecastTrace = {
                x: data.dates.slice(-30),
                y: data.future_predicted,
                type: 'scatter',
                mode: 'lines',
                name: '30-Day Forecast'
            };
            const forecastLayout = {
                title: '30-Day COVID-19 Case Forecast',
                xaxis: { title: 'Date' },
                yaxis: { title: 'Number of Cases' }
            };
            Plotly.newPlot('forecast-chart', [forecastTrace], forecastLayout);
            // Update performance metrics
            document.getElementById('mae').innerText = data.mae ? data.mae.toFixed(2) : 'N/A';
            document.getElementById('rmse').innerText = data.rmse ? data.rmse.toFixed(2) : 'N/A';
            document.getElementById('mape').innerText = data.mape && isFinite(data.mape) ? (data.mape.toFixed(2)) + '%' : 'N/A';
            document.getElementById('last-updated').innerText = data.last_updated ? dayjs(data.last_updated).format('MMMM D, YYYY') : 'N/A';
        })
        .catch(error => {
            console.error('Error fetching or processing data:', error);
            document.getElementById('prediction-chart').innerHTML = 'Error loading chart data: ' + error.message;
            document.getElementById('performance-metrics').innerHTML = 'Error loading performance metrics: ' + error.message;
            document.getElementById('forecast-chart').innerHTML = 'Error loading forecast data: ' + error.message;
        });
});
</script>
