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

For more details on our methodology, please visit our [GitHub repository](https://github.com/yourusername/covid-prediction).

<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/dayjs/1.10.4/dayjs.min.js"></script>
<script>
document.addEventListener('DOMContentLoaded', function() {
    // Fetch the latest prediction data
    fetch('/assets/data/covid_predictions.json')
        .then(response => response.json())
        .then(data => {
            // Create the prediction chart
            const trace1 = {
                x: data.dates,
                y: data.actual,
                type: 'scatter',
                mode: 'lines',
                name: 'Actual Cases'
            };
            const trace2 = {
                x: data.dates,
                y: data.predicted,
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
                <p>Mean Absolute Error: ${data.mae.toFixed(2)}</p>
                <p>Root Mean Square Error: ${data.rmse.toFixed(2)}</p>
                <p>Mean Absolute Percentage Error: ${(data.mape * 100).toFixed(2)}%</p>
                <p>Last Updated: ${dayjs(data.last_updated).format('MMMM D, YYYY')}</p>
            `;
        });
});
</script>