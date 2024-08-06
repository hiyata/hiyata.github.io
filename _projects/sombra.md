---
layout: default
title: System for Operational Modeling of Biological Replication and Adaptation (SOMBRA)
---

# HCMV Full Genome Sample Distribution


<div style="display: flex; flex-wrap: wrap; justify-content: space-between;">
    <div id="neuralNetworkAnimation" style="width: 100%; height: 400px; margin-bottom: 20px;"></div>
    <div id="mapid" style="height: 500px; width: 100%; margin-bottom: 20px;"></div>
    <div id="scatterPlot" style="height: 600px; width: 100%; margin-bottom: 20px;"></div>
    <div id="chartContainer" style="height: 400px; width: 48%;">
        <canvas id="sampleChart"></canvas>
    </div>
    <div id="strainList" style="height: 400px; width: 48%; overflow-y: auto;">
        <h3>Strain List</h3>
        <ul id="strainListContent"></ul>
    </div>
</div>

<div id="legend" style="margin-top: 20px;">
    <h3>Legend</h3>
    <div><span style="color: red; font-size: 20px;">●</span> Continent</div>
    <div><span style="color: orange; font-size: 20px;">●</span> Country</div>
    <div><span style="color: green; font-size: 20px;">●</span> State (USA only)</div>
</div>


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css"
   integrity="sha512-xodZBNTC5n17Xt2atTPuE1HxjVMSvLVW9ocqUKLsCC5CXdbqCmblAshOMAS6/keqq/sMZMZ19scR4PsZChSR7A=="
   crossorigin=""/>

<script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js"
   integrity="sha512-XQoYMqMTK8LvdxXYG3nZ448hOEQiglfqkJs1NOQV44cWnUrBc8PkAOcXy20w0vlaXaVUearIOBhiXZ5V3ynxwA=="
   crossorigin=""></script>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/PapaParse/5.3.0/papaparse.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/animejs/3.2.1/anime.min.js"></script>
<script src="https://d3js.org/d3.v7.min.js"></script>

<script>
// Global variables
let mymap, myChart, globalData, scatterPlot;
const continentCenters = {
    "Africa": [0, 20],
    "Europe": [50, 10],
    "Americas": [40, -100],
    "Asia": [35, 105],
    "Oceania": [-25, 135]
};

const countryCenters = {
    "Zambia": [-13.1339, 27.8493],
    "United Kingdom": [55.3781, -3.4360],
    "Germany": [51.1657, 10.4515],
    "France": [46.2276, 2.2137],
    "Belgium": [50.5039, 4.4699],
    "Israel": [31.0461, 34.8516],
    "Italy": [41.8719, 12.5674],
    "USA": [37.0902, -95.7129],
    "South Korea": [35.9078, 127.7669],
    "Czech Republic": [49.8175, 15.4730],
    "Australia": [-25.2744, 133.7751],
    "Greece": [39.0742, 21.8243],
    "Netherlands": [52.1326, 5.2913],
    "Uganda": [1.3733, 32.2903],
    "Kenya": [-0.0236, 37.9062],
    "South Africa": [-30.5595, 22.9375],
    "China": [35.8617, 104.1954],
    "Austria": [47.5162, 14.5501]
};

const stateCenters = {
    "North Carolina": [35.7596, -79.0193],
    "Virginia": [37.7693, -78.1700],
    "Ohio": [40.4173, -82.9071]
};

// Function to initialize the map
function initMap() {
    mymap = L.map('mapid').setView([20, 0], 2);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(mymap);

    mymap.on('click', resetView);
}

// Function to reset view to world map
function resetView() {
    mymap.setView([20, 0], 2);
    updateChart(
        Object.values(globalData.continents).map(c => c.count),
        Object.keys(globalData.continents)
    );
    updateStrainList(
        globalData.data.map(row => ({Strain: row.Strain, ID: row.ID})),
        'All Strains'
    );
}

// Function to update the chart
function updateChart(data, labels) {
    if (myChart) myChart.destroy();
    const ctx = document.getElementById('sampleChart').getContext('2d');
    myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: '# of Strains',
                data: data,
                backgroundColor: 'rgba(75, 192, 192, 0.6)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Number of Strains'
                    }
                }
            }
        }
    });
}

// Function to update the strain list
function updateStrainList(strains, title) {
    const strainListContent = document.getElementById('strainListContent');
    strainListContent.innerHTML = '';
    const titleElement = document.createElement('h4');
    titleElement.textContent = title;
    strainListContent.appendChild(titleElement);
    strains.forEach(strain => {
        const li = document.createElement('li');
        li.textContent = `${strain.Strain} (ID: ${strain.ID})`;
        strainListContent.appendChild(li);
    });
}

// Function to process CSV data
function processData(results) {
    const data = results.data.filter(row => row.Continent && row.Country && row.Strain && row.ID && row.Component1 && row.Component2);
    const continents = {};
    const countries = {};
    const states = {};

    data.forEach(row => {
        if (!continents[row.Continent]) {
            continents[row.Continent] = { count: 0, countries: {}, strains: new Set() };
        }
        if (!continents[row.Continent].countries[row.Country]) {
            continents[row.Continent].countries[row.Country] = { count: 0, strains: new Set(), states: {} };
        }
        if (!countries[row.Country]) {
            countries[row.Country] = { continent: row.Continent, count: 0, strains: new Set(), states: {} };
        }
        if (row.State && row.Country === 'USA') {
            if (!continents[row.Continent].countries[row.Country].states[row.State]) {
                continents[row.Continent].countries[row.Country].states[row.State] = { count: 0, strains: new Set() };
            }
            if (!countries[row.Country].states[row.State]) {
                countries[row.Country].states[row.State] = { count: 0, strains: new Set() };
            }
            if (!states[row.State]) {
                states[row.State] = { count: 0, strains: new Set() };
            }
            continents[row.Continent].countries[row.Country].states[row.State].count++;
            continents[row.Continent].countries[row.Country].states[row.State].strains.add(JSON.stringify({Strain: row.Strain, ID: row.ID}));
            countries[row.Country].states[row.State].count++;
            countries[row.Country].states[row.State].strains.add(JSON.stringify({Strain: row.Strain, ID: row.ID}));
            states[row.State].count++;
            states[row.State].strains.add(JSON.stringify({Strain: row.Strain, ID: row.ID}));
        }

        continents[row.Continent].count++;
        continents[row.Continent].countries[row.Country].count++;
        continents[row.Continent].strains.add(JSON.stringify({Strain: row.Strain, ID: row.ID}));
        continents[row.Continent].countries[row.Country].strains.add(JSON.stringify({Strain: row.Strain, ID: row.ID}));
        countries[row.Country].count++;
        countries[row.Country].strains.add(JSON.stringify({Strain: row.Strain, ID: row.ID}));
    });

    return { continents, countries, states, data };
}

// Function to create map markers
function createMarkers(data) {
    Object.entries(data.continents).forEach(([continent, contData]) => {
        const marker = L.circle(continentCenters[continent], {
            color: 'red',
            fillColor: '#f03',
            fillOpacity: 0.5,
            radius: Math.sqrt(contData.count) * 100000
        }).addTo(mymap);

        marker.bindPopup(continent);
        marker.on('click', (e) => {
            e.originalEvent.stopPropagation();  // Prevent triggering map click
            mymap.flyTo(continentCenters[continent], 4);
            updateChart(
                Object.values(contData.countries).map(c => c.count),
                Object.keys(contData.countries)
            );
            updateStrainList(
                Array.from(contData.strains).map(s => JSON.parse(s)),
                `Strains in ${continent}`
            );
            createCountryMarkers(contData.countries, continent);
        });
    });
}

// Function to create country markers
function createCountryMarkers(countries, continent) {
    Object.entries(countries).forEach(([country, countryData]) => {
        if (countryCenters[country]) {
            const countryMarker = L.circleMarker(countryCenters[country], {
                radius: Math.sqrt(countryData.count) * 2,
                fillColor: "orange",
                color: "#000",
                weight: 1,
                opacity: 1,
                fillOpacity: 0.8
            }).addTo(mymap);

            countryMarker.bindPopup(`${country}: ${countryData.count} strains`);
            countryMarker.on('click', (e) => {
                e.originalEvent.stopPropagation();  // Prevent triggering map click
                if (country === 'USA') {
                    mymap.flyTo(countryCenters[country], 5);
                    createStateMarkers(countryData.states);
                    updateChart(
                        Object.values(countryData.states).map(s => s.count),
                        Object.keys(countryData.states)
                    );
                } else {
                    updateStrainList(
                        Array.from(countryData.strains).map(s => JSON.parse(s)),
                        `Strains in ${country}`
                    );
                }
            });
        }
    });
}

// Function to create state markers (for USA)
function createScatterPlot(data) {
    const scatterPlot = document.getElementById('scatterPlot');
    const width = scatterPlot.clientWidth;
    const height = scatterPlot.clientHeight;
    const margin = { top: 60, right: 140, bottom: 80, left: 80 };
    const plotWidth = width - margin.left - margin.right;
    const plotHeight = height - margin.top - margin.bottom;

    const svg = d3.select('#scatterPlot')
        .append('svg')
        .attr('width', width)
        .attr('height', height);

    const g = svg.append('g')
        .attr('transform', `translate(${margin.left},${margin.top})`);

    // Filter out outliers (using IQR method)
    const q1x = d3.quantile(data.map(d => parseFloat(d.Component1)).sort(d3.ascending), 0.25);
    const q3x = d3.quantile(data.map(d => parseFloat(d.Component1)).sort(d3.ascending), 0.75);
    const iqrx = q3x - q1x;
    const q1y = d3.quantile(data.map(d => parseFloat(d.Component2)).sort(d3.ascending), 0.25);
    const q3y = d3.quantile(data.map(d => parseFloat(d.Component2)).sort(d3.ascending), 0.75);
    const iqry = q3y - q1y;

    const filteredData = data.filter(d => 
        parseFloat(d.Component1) >= q1x - 1.5 * iqrx &&
        parseFloat(d.Component1) <= q3x + 1.5 * iqrx &&
        parseFloat(d.Component2) >= q1y - 1.5 * iqry &&
        parseFloat(d.Component2) <= q3y + 1.5 * iqry
    );

    // Add padding to the domain
    const xExtent = d3.extent(filteredData, d => parseFloat(d.Component1));
    const yExtent = d3.extent(filteredData, d => parseFloat(d.Component2));
    const xPadding = (xExtent[1] - xExtent[0]) * 0.1;
    const yPadding = (yExtent[1] - yExtent[0]) * 0.1;

    const x = d3.scaleLinear()
        .domain([xExtent[0] - xPadding, xExtent[1] + xPadding])
        .range([0, plotWidth]);

    const y = d3.scaleLinear()
        .domain([yExtent[0] - yPadding, yExtent[1] + yPadding])
        .range([plotHeight, 0]);

    const color = d3.scaleOrdinal()
        .domain(['Africa', 'Asia', 'Europe', 'Americas', 'Oceania'])
        .range(['orange', '#FF1493', 'darkblue', '#8B008B', 'green']);

    const xAxis = d3.axisBottom(x);
    const yAxis = d3.axisLeft(y);

    g.append('g')
        .attr('class', 'x-axis')
        .attr('transform', `translate(0,${plotHeight})`)
        .call(xAxis);

    g.append('g')
        .attr('class', 'y-axis')
        .call(yAxis);

    g.append('text')
        .attr('class', 'axis-label')
        .attr('x', plotWidth / 2)
        .attr('y', plotHeight + 60)
        .attr('fill', '#000')
        .attr('text-anchor', 'middle')
        .attr('font-size', '16px')
        .text('Component 1');

    g.append('text')
        .attr('class', 'axis-label')
        .attr('transform', 'rotate(-90)')
        .attr('y', -60)
        .attr('x', -plotHeight / 2)
        .attr('dy', '1em')
        .attr('fill', '#000')
        .attr('text-anchor', 'middle')
        .attr('font-size', '16px')
        .text('Component 2');

    // Add ellipses for each continent
    const continentGroups = d3.group(filteredData, d => d.Continent);
    continentGroups.forEach((points, continent) => {
        const x_values = points.map(d => parseFloat(d.Component1));
        const y_values = points.map(d => parseFloat(d.Component2));
        const [cx, cy] = [d3.mean(x_values), d3.mean(y_values)];
        const [rx, ry] = [d3.deviation(x_values) * 1.5, d3.deviation(y_values) * 1.5];

        const ellipse = g.append('ellipse')
            .attr('cx', x(cx))
            .attr('cy', y(cy))
            .attr('rx', Math.min(x(cx + rx) - x(cx), plotWidth / 2))
            .attr('ry', Math.min(y(cy) - y(cy + ry), plotHeight / 2))
            .attr('fill', 'none')
            .attr('stroke', color(continent))
            .attr('stroke-width', 2)
            .attr('opacity', 0);

        // Animate ellipses appearing
        anime({
            targets: ellipse.node(),
            opacity: 0.3,
            strokeDashoffset: [anime.setDashoffset, 0],
            easing: 'easeInOutSine',
            duration: 2000,
            delay: 1000
        });
    });

    const points = g.selectAll('.point')
        .data(filteredData)
        .enter().append('circle')
        .attr('class', 'point')
        .attr('r', 4)
        .attr('cx', d => x(parseFloat(d.Component1)))
        .attr('cy', d => y(parseFloat(d.Component2)))
        .attr('fill', d => color(d.Continent))
        .attr('stroke', '#fff')
        .attr('stroke-width', 1)
        .attr('opacity', 0);

    // Animate points appearing
    anime({
        targets: points.nodes(),
        opacity: 0.8,
        scale: [0, 1],
        delay: anime.stagger(10),
        easing: 'easeOutElastic(1, .5)',
        duration: 1500
    });

    // Add legend
    const legendBackground = svg.append('rect')
        .attr('x', width - margin.right + 10)
        .attr('y', margin.top)
        .attr('width', margin.right - 20)
        .attr('height', 110)
        .attr('fill', 'white')
        .attr('stroke', 'black');

    const legend = svg.append('g')
        .attr('class', 'legend')
        .attr('transform', `translate(${width - margin.right + 20}, ${margin.top + 10})`);

    const continents = ['Africa', 'Asia', 'Europe', 'Americas', 'Oceania'];

    legend.selectAll('rect')
        .data(continents)
        .enter()
        .append('rect')
        .attr('y', (d, i) => i * 20)
        .attr('width', 10)
        .attr('height', 10)
        .attr('fill', d => color(d));

    legend.selectAll('text')
        .data(continents)
        .enter()
        .append('text')
        .attr('x', 15)
        .attr('y', (d, i) => i * 20 + 9)
        .text(d => d)
        .attr('font-size', '12px')
        .attr('alignment-baseline', 'middle');

    // Add tooltip in bottom right corner
    const tooltip = g.append('text')
        .attr('class', 'tooltip')
        .attr('x', plotWidth - 10)
        .attr('y', plotHeight - 10)
        .attr('text-anchor', 'end')
        .attr('font-size', '12px')
        .attr('fill', 'black')
        .style('opacity', 0);

    // Add interactivity
    points.on('mouseover', function(event, d) {
        d3.select(this)
            .transition()
            .duration(200)
            .attr('r', 8)
            .attr('stroke-width', 2);

        tooltip.text(`${d.Strain} (${d.Country})`)
            .style('opacity', 1);
    }).on('mouseout', function() {
        d3.select(this)
            .transition()
            .duration(200)
            .attr('r', 4)
            .attr('stroke-width', 1);

        tooltip.style('opacity', 0);
    });
}

// Main function to load and process data
function loadData() {
    Papa.parse('hcmv_strains.csv', {
        download: true,
        header: true,
        complete: function(results) {
            globalData = processData(results);
            createMarkers(globalData);
            updateChart(
                Object.values(globalData.continents).map(c => c.count),
                Object.keys(globalData.continents)
            );
            updateStrainList(
                globalData.data.map(row => ({Strain: row.Strain, ID: row.ID})),
                'All Strains'
            );
            createScatterPlot(globalData.data);
        }
    });
}

// Neural Network Animation
function createNeuralNetworkAnimation() {
    const container = document.getElementById('neuralNetworkAnimation');
    const width = container.clientWidth;
    const height = container.clientHeight;

    // Create SVG
    const svg = d3.select('#neuralNetworkAnimation')
        .append('svg')
        .attr('width', width)
        .attr('height', height);

    // Define colors
    const colors = {
        kmer: ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00'],
        layers: ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854']
    };

    // Phase 1: DNA Sequence and K-mers
    const dnaSequence = 'ATCGATCGATCGATCGACTGATCGATCGATCG';
    const kmerSize = 6;

    const dnaText = svg.append('text')
        .attr('x', width / 2)
        .attr('y', height / 2)
        .attr('text-anchor', 'middle')
        .attr('class', 'dna-sequence')
        .attr('font-size', '24px')
        .attr('font-weight', 'bold')
        .text(dnaSequence);

    function breakIntoKmers() {
        dnaText.remove();
        const kmers = [];
        for (let i = 0; i <= dnaSequence.length - kmerSize; i++) {
            kmers.push(dnaSequence.substr(i, kmerSize));
        }

        kmers.forEach((kmer, index) => {
            svg.append('text')
                .attr('x', width / 2)
                .attr('y', height / 2 + index * 30 - (kmers.length * 15))
                .attr('text-anchor', 'middle')
                .attr('class', 'kmer')
                .attr('font-size', '18px')
                .attr('fill', colors.kmer[index % colors.kmer.length])
                .text(kmer);
        });

        return kmers;
    }

    // Phase 2: Neural Network
    const layers = [
        {name: 'Input', nodes: 6},
        {name: 'Hidden1', nodes: 8},
        {name: 'Hidden2', nodes: 6},
        {name: 'Hidden3', nodes: 4},
        {name: 'Output', nodes: 2}
    ];

    function createNeuralNetwork() {
        svg.selectAll('*').remove();
        const layerWidth = width / (layers.length + 1);

        layers.forEach((layer, layerIndex) => {
            const nodeSpacing = height / (layer.nodes + 1);
            for (let i = 0; i < layer.nodes; i++) {
                svg.append('circle')
                    .attr('cx', (layerIndex + 1) * layerWidth)
                    .attr('cy', (i + 1) * nodeSpacing)
                    .attr('r', 10)
                    .attr('fill', colors.layers[layerIndex])
                    .attr('stroke', '#333')
                    .attr('class', `node layer${layerIndex}`)
                    .style('opacity', 0);
            }
        });

        for (let i = 0; i < layers.length - 1; i++) {
            const startNodes = svg.selectAll(`.layer${i}`);
            const endNodes = svg.selectAll(`.layer${i+1}`);
            
            startNodes.each(function(_, startIndex) {
                const start = d3.select(this);
                endNodes.each(function(_, endIndex) {
                    const end = d3.select(this);
                    svg.append('line')
                        .attr('x1', start.attr('cx'))
                        .attr('y1', start.attr('cy'))
                        .attr('x2', end.attr('cx'))
                        .attr('y2', end.attr('cy'))
                        .attr('stroke', '#999')
                        .attr('stroke-width', 1)
                        .attr('class', 'connection')
                        .style('opacity', 0);
                });
            });
        }

        layers.forEach((layer, index) => {
            svg.append('text')
                .attr('x', (index + 1) * layerWidth)
                .attr('y', height - 10)
                .attr('text-anchor', 'middle')
                .text(layer.name)
                .style('opacity', 0);
        });
    }

    // Phase 3: Decision
    function showDecision() {
        svg.selectAll('*').remove();
        const lastHiddenLayer = layers[layers.length - 2];
        const outputLayer = layers[layers.length - 1];

        const nodeRadius = 20;
        const layerSpacing = width / 3;

        // Draw last hidden layer
        lastHiddenLayer.nodes.forEach((_, i) => {
            svg.append('circle')
                .attr('cx', layerSpacing)
                .attr('cy', (i + 1) * (height / (lastHiddenLayer.nodes + 1)))
                .attr('r', nodeRadius)
                .attr('fill', colors.layers[layers.length - 2]);
        });

        // Draw output layer
        const outputs = ['DNA Correction Required', 'DNA Stable'];
        outputLayer.nodes.forEach((_, i) => {
            svg.append('circle')
                .attr('cx', 2 * layerSpacing)
                .attr('cy', (i + 1) * (height / (outputLayer.nodes + 1)))
                .attr('r', nodeRadius)
                .attr('fill', colors.layers[layers.length - 1]);

            svg.append('text')
                .attr('x', 2 * layerSpacing + nodeRadius + 10)
                .attr('y', (i + 1) * (height / (outputLayer.nodes + 1)))
                .attr('dominant-baseline', 'middle')
                .attr('font-size', '16px')
                .text(outputs[i]);
        });

        // Draw connections
        lastHiddenLayer.nodes.forEach((_, i) => {
            outputLayer.nodes.forEach((_, j) => {
                svg.append('line')
                    .attr('x1', layerSpacing)
                    .attr('y1', (i + 1) * (height / (lastHiddenLayer.nodes + 1)))
                    .attr('x2', 2 * layerSpacing)
                    .attr('y2', (j + 1) * (height / (outputLayer.nodes + 1)))
                    .attr('stroke', '#999')
                    .attr('stroke-width', 1);
            });
        });

        // Highlight decision
        const decision = Math.random() < 0.5 ? 0 : 1;
        svg.select(`circle:nth-child(${layers.length + decision + 1})`)
            .transition()
            .duration(1000)
            .attr('r', nodeRadius * 1.2)
            .attr('stroke', '#333')
            .attr('stroke-width', 3);
    }

    // Animation timeline
    function runAnimation() {
        // Phase 1
        anime({
            targets: '.dna-sequence',
            opacity: [0, 1],
            duration: 1000,
            easing: 'easeInOutQuad',
            complete: () => {
                const kmers = breakIntoKmers();
                anime({
                    targets: '.kmer',
                    translateY: (el, i) => [100, 0],
                    opacity: [0, 1],
                    delay: anime.stagger(100),
                    duration: 1000,
                    easing: 'easeOutElastic(1, .5)',
                    complete: () => {
                        // Phase 2
                        anime({
                            targets: '.kmer',
                            translateX: -width / 2 + 100,
                            opacity: 0,
                            duration: 1000,
                            easing: 'easeInOutQuad',
                            complete: () => {
                                createNeuralNetwork();
                                anime({
                                    targets: '.node',
                                    scale: [0, 1],
                                    opacity: 1,
                                    delay: anime.stagger(100, {grid: [layers.length, 8], from: 'first'}),
                                    duration: 800,
                                    easing: 'easeOutElastic(1, .5)',
                                    complete: () => {
                                        anime({
                                            targets: '.connection',
                                            opacity: 1,
                                            strokeDashoffset: [anime.setDashoffset, 0],
                                            delay: anime.stagger(10),
                                            duration: 1000,
                                            easing: 'easeInOutSine',
                                            complete: () => {
                                                // Phase 3
                                                showDecision();
                                            }
                                        });
                                    }
                                });

                                anime({
                                    targets: 'text',
                                    opacity: 1,
                                    duration: 1000,
                                    easing: 'easeInOutQuad'
                                });
                            }
                        });
                    }
                });
            }
        });
    }

    runAnimation();
}

// Call the function to create and start the animation
createNeuralNetworkAnimation();

// Initialize everything
initMap();
loadData();
</script>