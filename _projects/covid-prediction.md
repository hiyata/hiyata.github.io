---
layout: page
title: COVID-19 Case Prediction Model
excerpt: Weekly forecast of global COVID-19 cases
permalink: /covid-prediction/
---

# COVID-19 Case Prediction Model

This page displays an 8-week forecast of global COVID-19 cases, updated weekly. Our model is trained on historical data and makes predictions for the next two months. The graph below shows our predictions against the actual reported weekly cases.

<div id="prediction-chart"></div>

## Model Performance

Our model's performance is evaluated weekly. Below are some key metrics:

<div id="performance-metrics"></div>

## Methodology

We use Facebook's Prophet model for time series forecasting. The model is trained on COVID-19 case data from Our World in Data, which is updated regularly. Our prediction pipeline follows these steps:

1. Weekly data collection and aggregation from the Our World in Data COVID-19 dataset
2. Data cleaning to remove zero or missing values
3. Model retraining with the latest available data
4. 8-week forecast generation
5. Weekly comparison of predictions with actual reported cases

For more details on our methodology, please visit our [GitHub repository](https://github.com/hiyata/covid-19-prediction).

<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/dayjs/1.10.4/dayjs.min.js"></script>
<script>
document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM content loaded');
    fetch('/assets/covid-19-files/covid_predictions.json')
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log('Parsed data:', data);
            // Filter out null values from actual data
            const actualData = data.actual.map((value, index) => value ? {x: data.dates[index], y: value} : null).filter(Boolean);            
            const trace1 = {
                x: actualData.map(point => point.x),
                y: actualData.map(point => point.y),
                type: 'scatter',
                mode: 'markers',
                name: 'Actual Weekly Cases'
            };
            const trace2 = {
                x: data.dates,
                y: data.predicted,
                type: 'scatter',
                mode: 'lines',
                name: 'Predicted Weekly Cases'
            };
            const layout = {
                title: 'COVID-19 Weekly Cases: Actual vs Predicted',
                xaxis: { title: 'Date' },
                yaxis: { title: 'Number of Weekly Cases' }
            };
            Plotly.newPlot('prediction-chart', [trace1, trace2], layout);       
            const metricsDiv = document.getElementById('performance-metrics');
            metricsDiv.innerHTML = `
                <p>Mean Absolute Error: ${data.mae ? data.mae.toFixed(2) : 'N/A'}</p>
                <p>Root Mean Square Error: ${data.rmse ? data.rmse.toFixed(2) : 'N/A'}</p>
                <p>Mean Absolute Percentage Error: ${data.mape && isFinite(data.mape) ? (data.mape * 100).toFixed(2) + '%' : 'N/A'}</p>
                <p>Last Updated: ${data.last_updated ? dayjs(data.last_updated).format('MMMM D, YYYY') : 'N/A'}</p>
            `;
        })
        .catch(error => {
            console.error('Error fetching or processing data:', error);
            document.getElementById('prediction-chart').innerHTML = 'Error loading chart data: ' + error.message;
            document.getElementById('performance-metrics').innerHTML = 'Error loading performance metrics: ' + error.message;
        });
});
</script>