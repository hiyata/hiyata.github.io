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

<div id="performance-metrics" class="metrics-container">
    <div class="metric-card">
        <h3>Mean Absolute Error</h3>
        <p id="mae" class="metric-value">N/A</p>
    </div>
    <div class="metric-card">
        <h3>Root Mean Square Error</h3>
        <p id="rmse" class="metric-value">N/A</p>
    </div>
    <div class="metric-card">
        <h3>Mean Absolute Percentage Error</h3>
        <p id="mape" class="metric-value">N/A</p>
    </div>
    <div class="metric-card">
        <h3>Last Updated</h3>
        <p id="last-updated" class="metric-value">N/A</p>
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
<script src="https://cdnjs.cloudflare.com/ajax/libs/animejs/3.2.1/anime.min.js"></script>

<style>
.metrics-container {
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
    margin-top: 20px;
}
.metric-card {
    background: linear-gradient(145deg, #f3f4f6, #ffffff);
    border-radius: 15px;
    box-shadow: 5px 5px 15px #d1d9e6, -5px -5px 15px #ffffff;
    padding: 20px;
    width: 200px;
    margin: 10px;
    text-align: center;
    transition: transform 0.3s ease;
}
.metric-card:hover {
    transform: translateY(-5px);
}
.metric-value {
    font-size: 24px;
    font-weight: bold;
    color: #4a5568;
    margin-top: 10px;
}
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM content loaded');
    fetch('/assets/covid-19-files/covid_predictions.json')
        .then(response => {
            console.log('Response status:', response.status);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log('Data received:', data);
            if (!data || !Array.isArray(data.dates) || !Array.isArray(data.actual) || !Array.isArray(data.predicted)) {
                throw new Error('Data is missing required fields or they are not arrays');
            }
            
            // Create the prediction chart
            const trace1 = {
                x: data.dates,
                y: data.actual,
                type: 'scatter',
                mode: 'lines',
                name: 'Actual Cases',
                line: {color: '#3182CE'}
            };
            const trace2 = {
                x: data.dates,
                y: data.predicted,
                type: 'scatter',
                mode: 'lines',
                name: 'Predicted Cases',
                line: {color: '#E53E3E'}
            };
            const layout = {
                title: 'COVID-19 Cases: Actual vs Predicted',
                xaxis: { title: 'Date', rangeslider: {visible: true} },
                yaxis: { title: 'Number of Cases' },
                plot_bgcolor: '#F7FAFC',
                paper_bgcolor: '#F7FAFC',
                hovermode: 'closest'
            };
            Plotly.newPlot('prediction-chart', [trace1, trace2], layout);

            // Animate the lines
            anime({
                targets: '#prediction-chart path.js-line',
                strokeDashoffset: [anime.setDashoffset, 0],
                easing: 'easeInOutSine',
                duration: 1500,
                delay: function(el, i) { return i * 250 },
                direction: 'alternate',
                loop: false
            });

            // Create the forecast chart
            const forecastTrace = {
                x: data.future_dates,
                y: data.future_predicted,
                type: 'scatter',
                mode: 'lines',
                name: '30-Day Forecast',
                line: {color: '#38A169'}
            };
            const forecastLayout = {
                title: '30-Day COVID-19 Case Forecast',
                xaxis: { title: 'Date' },
                yaxis: { title: 'Number of Cases' },
                plot_bgcolor: '#F7FAFC',
                paper_bgcolor: '#F7FAFC',
                hovermode: 'closest'
            };
            Plotly.newPlot('forecast-chart', [forecastTrace], forecastLayout);

            // Animate the forecast line
            anime({
                targets: '#forecast-chart path.js-line',
                strokeDashoffset: [anime.setDashoffset, 0],
                easing: 'easeInOutSine',
                duration: 1500,
                delay: 1000,
                direction: 'alternate',
                loop: false
            });

            // Update performance metrics with animation
            const metrics = ['mae', 'rmse', 'mape', 'last-updated'];
            metrics.forEach(metric => {
                let el = document.getElementById(metric);
                let value = data[metric];
                if (metric === 'mape' && isFinite(value)) {
                    value = value.toFixed(2) + '%';
                } else if (metric === 'last-updated') {
                    value = dayjs(value).format('MMMM D, YYYY');
                } else if (typeof value === 'number') {
                    value = value.toFixed(2);
                }
                el.innerText = '0';
                anime({
                    targets: el,
                    innerHTML: [0, value],
                    round: 1,
                    easing: 'easeInOutExpo',
                    duration: 2000
                });
            });
        })
        .catch(error => {
            console.error('Error fetching or processing data:', error);
            document.getElementById('prediction-chart').innerHTML = 'Error loading chart data: ' + error.message;
            document.getElementById('performance-metrics').innerHTML = 'Error loading performance metrics: ' + error.message;
            document.getElementById('forecast-chart').innerHTML = 'Error loading forecast data: ' + error.message;
        });
});
</script>