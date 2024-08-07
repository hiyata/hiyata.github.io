---
layout: page
title: COVID-19 Case Prediction Model
excerpt: This is a brief summary of the project.
permalink: /covid-prediction/
---

# COVID-19 Case Prediction Model

This page displays a 30-day forecast of COVID-19 cases, updated daily. Our model is trained on historical data and makes predictions for the next month. The graph below shows our predictions against the actual reported cases.

<div id="prediction-chart"></div>

## Model Performance

Our model's performance is evaluated daily. Below are some key metrics:

<div id="performance-metrics"></div>

## Methodology

We use Facebook's Prophet model for time series forecasting. The model is trained on COVID-19 case data from Johns Hopkins University, which is updated daily. Our prediction pipeline follows these steps:

1. Daily data collection from JHU CSSE COVID-19 dataset
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
            return response.text();  // Get the response as text
        })
        .then(text => {
            console.log('Data received (first 100 chars):', text.substring(0, 100));
            // Sanitize and parse the JSON
            try {
                // Remove potential trailing characters and replace Infinity with null
                const sanitizedText = text.replace(/Infinity/g, 'null');
                const jsonDataString = sanitizedText.substring(0, sanitizedText.lastIndexOf('}') + 1);
                const data = JSON.parse(jsonDataString);                
                console.log('Parsed data:', data);               
                if (!data || !Array.isArray(data.dates) || !Array.isArray(data.actual) || !Array.isArray(data.predicted)) {
                    throw new Error('Data is missing required fields or they are not arrays');
                }                
                // Filter out entries with zero values
                const filteredData = {
                    dates: [],
                    actual: [],
                    predicted: []
                };
                for (let i = 0; i < data.dates.length; i++) {
                    if (data.actual[i] !== 0 || data.predicted[i] !== 0) {
                        filteredData.dates.push(data.dates[i]);
                        filteredData.actual.push(data.actual[i]);
                        filteredData.predicted.push(data.predicted[i]);
                    }
                }               
                // Create the prediction chart
                const trace1 = {
                    x: filteredData.dates,
                    y: filteredData.actual,
                    type: 'scatter',
                    mode: 'lines',
                    name: 'Actual Cases'
                };
                const trace2 = {
                    x: filteredData.dates,
                    y: filteredData.predicted,
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
                // Update performance metrics
                const metricsDiv = document.getElementById('performance-metrics');
                metricsDiv.innerHTML = `
                    <p>Mean Absolute Error: ${data.mae ? data.mae.toFixed(2) : 'N/A'}</p>
                    <p>Root Mean Square Error: ${data.rmse ? data.rmse.toFixed(2) : 'N/A'}</p>
                    <p>Mean Absolute Percentage Error: ${data.mape && isFinite(data.mape) ? (data.mape * 100).toFixed(2) + '%' : 'N/A'}</p>
                    <p>Last Updated: ${data.last_updated ? dayjs(data.last_updated).format('MMMM D, YYYY') : 'N/A'}</p>
                `;
            } catch (error) {
                console.error('Error parsing JSON:', error);
                throw new Error('Failed to parse JSON data');
            }
        })
        .catch(error => {
            console.error('Error fetching or processing data:', error);
            document.getElementById('prediction-chart').innerHTML = 'Error loading chart data: ' + error.message;
            document.getElementById('performance-metrics').innerHTML = 'Error loading performance metrics: ' + error.message;
        });
});
</script>
