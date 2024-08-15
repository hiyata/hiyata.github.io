---
layout: default
category: virology
excerpt: A system to generate artificial HCMV genomes and simulate evolution to characterize geographical strain diversity. 
title: System for Operational Modeling of Biological Replication and Adaptation (SOMBRA)
presented_at: IHW 2024
---

<h1 style="text-align: center;">SOMBRA</h1>
---
Study of human cytomegalovirus (HCMV) evolution is crucial for understanding its genetic diversity, adaptation mechanisms, and impact on human health. Existing phylogenetic analyses of HCMV have begun to reveal important evolutionary patterns and relationships among geographically distinct strains, as demonstrated in recent works by Charles and Venturini et al. (1). However, the geographic resolution of phylogenetic analyses is limited by (i) the small number of publicly available complete HCMV genomes—351 in NCBI Virus, and (ii) the uneven geographic distribution of those sequences. 

## Dataset 

The map below displays the geographical locations where each was collected. Their strains and ID are attached as well. 

<div style="display: flex; flex-wrap: wrap; justify-content: space-between;">
    <div style="width: 60%;">
        <div id="mapid" class="animate" style="height: 500px; width: 100%; margin-bottom: 20px;"></div>
        <div id="legend" class="animate" style="margin-top: 10px;">
            <h3>Legend</h3>
            <div><span style="color: red; font-size: 10px;">●</span> Continent</div>
            <div><span style="color: orange; font-size: 10px;">●</span> Country</div>
            <div><span style="color: green; font-size: 10px;">●</span> State (USA only)</div>
        </div>
    </div>
    <div style="width: 38%;">
        <div id="chartContainer" class="animate" style="height: 400px; width: 100%;">
            <canvas id="sampleChart"></canvas>
        </div>
        <div id="strainList" class="animate" style="height: 200px; width: 100%; overflow-y: auto; margin-top: 20px;">
            <h3>Strain List</h3>
            <ul id="strainListContent"></ul>
        </div>
    </div>
</div>

<br>

<h1 style="text-align: center;font-size: 25px;">System for Operational Modeling of Biological Replication and Adaptation (SOMBRA)</h1>

SOMBRA uses a sliding window approach to extract trends and identify conserved regions across the alignment. For windows with less than 90% agreement, consensus voting is used to assign a nucleotide for a particular position.

A k-mer index is generated from the MAFFT alignment to enable rapid alignment of each newly generated sequence with the reference alignment.

The country where each sample was isolated was included in the header of each sequence, and the continent extrapolated for each country. SOMBRA extracted this data and organized each sequence into a group. 

Once groups of sequences are assigned based on their continental origins, an ancestral sequences were generated for each continent. These sequences were constructed using the information extracted during initialization. Variable positions are determine by consensus voting across each continental group.  

The inferred ancestral sequence for each continent serve as inputs.  This begins by aligning the ancestral and reference sequences to ensure consistency. For each continent, the average variability is calculated from differences between the ancestral sequence and the reference sequences from the same continent. 

This average variability determines the number of mutations to apply to the ancestral sequence to simulate evolutionary changes. Precomputed base frequencies for each position guide substitutions by providing probabilities for each base at each position. Positions within indel hotspots are subjected to stochastic insertions or deletions.

Additionally, recombination events are simulated by mixing segments from different sequences at random breakpoints, further increasing genetic diversity.  The final synthetic sequences are saved to FASTA and TSV files. Future versions will integrate generative models to further improve biological relevance of the new sequences. 

<div id="neuralNetwork" style="width: 100%; height: 400px; position: relative;"></div>

## Simulated HCMV Genomes Have Ancestral Patterns That Parallel Clinical Samples 

<br>

<div style="display: flex; flex-wrap: wrap; justify-content: space-between;">
    <div id="scatterPlot" class="animate" style="height: 600px; width: 100%; margin-bottom: 20px;"></div>
</div>

### MDS Scatterplot


The scatterplot above depicts a multidimensional scaling (MDS) analyis of the merged reference dataset reveals genomic clusters associated with the continent where each sample was collected. Notably, clustering of African strains clustered on the peripheral of the European strains. Strains from the Americas cluster near Europe, however they have a larger range. This is consistent with findings published recently (1). 

### Generating Artificial HCMV Genomes

![artificial_HCMV_MDS](images/artificial_HCMV_MDS.png)

SOMBRA generated artificial HCMV genomes largely follow this pattern, with African clustering at the periphery of the European and American groups. Panel a depicts the original output from the MDS analyses. Panel b depicts an inversion of point positions around the centroid, revealing similar patterns with Asian, African, and Oceanic strains on the peripheral of  European and American strains at the center.     

![artificial_HCMV_MDS](images/artificial_reference_genome_size_HCMV.png)

Fig. 3 panel A depicts a length comparison between an generated African strain and a reference African strain. There is a notable size difference (~25%). Panel B displays a protein prediction comparison between memberane spanning protein US21, showing that generated strain contain the ORF, however terminates early. We suspect this is a likely result of inaccurate k-mer indexing we are working to correct.  

![artificial_US21](images/artificial_US21.png)

Panels C and D of Fig. 3 depict the results of a comparison of the genetic distances of every sequence, grouping by continent. Artificial sequences within continent show high in-group similarity, however, genetic distance between groups is higher. Notably, for both datasets, American derived genomes display a higher genetic distance.

![distribution_of_artificial_HCMV](images/distribution_of_artificial_HCMV.png)

![distribution_of_reference_HCMV](images/distribution_of_reference_HCMV.png)

![phylogenetic_tree_artificial_HCMV](images/phylogenetic_tree_artificial_HCMV.png)

Despite the size challenges, generated sequences display distinct lineage patterns (Fig. 4). The difference in the branch lengths between each continent are a reflection of existing diversity distributions within the reference. Overrepresentation of reference strains for both Europe and the Americas allow for a much more variable distribution of their generated counterparts. 

## Towards Neural Network Integration and a Multi-Agent System

There are trade-offs for rules-based and LLM-based simulations. Rules-based simulations are programmed with explicit instructions and offer interpretable results. Because the instructions are explicit, predictions are bounded by our current understanding of genomic patterns. 

Neural networks are often referred to as "black boxes" because of the difficultly in understanding how complex relationships between seemingly unrelated variables are formed during training. Nonetheless, they can help guide the development of hypothesis-based experiments to explain underlying biological realities connected to machine-learned patterns. 

Though LLMs present a massive leap for natural language processing, it is up to our community test and adapt these models to answer tackle biological questions. 

## MambaVirus, SOMBRA, and the Future

The context problem poses a challenge to Herpesvirus researchers' ability utilize LLMs. As machine learning researchers continue to tackle the context length problem in other realms, we should continue to adapt their findings to answer our biological questions in our realm. 

The progress in increasing context size, as illustrated by HyenaDNA (5) in the left panel of Fig. 6, demonstrates how researchers are adapting state-of-the-art architectures to address this challenge. We have taken an analogous approach with Mamba. 

Model architectures vary and are useful for different tasks. The differences between BERT and Mamba architectures (Figs. 5 and 7) guide our usage of them. 

VIRUSBERT's success in DNA classification tasks makes it a candidate for use to detect fatal mutation 
in DNA. We are currently compiling a dataset to fine-tune VIRUSBERT for this purpose. 

In addition to VIRUSBERT, we foresee MambaVirus as a tool to correct and regenerate sequences identified by VIRUSBERT. 

Integrating our trained language models could greatly improve SOMBRA's ability to generate new genomes. We are continously training and testing new models for integration. Future development of SOMBRA aims to tackle broken protein sequences (Fig. 3, panel b), and develop autonomous agents that function independantly to make gene modifications. 

With this, we hope that the continued development of SOMBRA leads to a powerful tool to model evolution.  

<script src="https://cdnjs.cloudflare.com/ajax/libs/animejs/3.2.1/anime.min.js"></script>

<script>
// Neural network animation
function createNeuralNetworkAnimation() {
    const container = document.getElementById('neuralNetwork');
    const width = container.clientWidth;
    const height = container.clientHeight;
    
    const layers = [
        { name: 'Input', nodes: 4, color: '#3498db' },
        { name: 'Hidden 1', nodes: 6, color: '#e74c3c' },
        { name: 'Hidden 2', nodes: 6, color: '#2ecc71' },
        { name: 'Output', nodes: 4, color: '#f39c12' }
    ];
    const nodeRadius = 15;
    const layerSpacing = width / (layers.length + 1);
    
    // Create connections and nodes
    layers.forEach((layer, layerIndex) => {
        // Create layer label
        const label = document.createElement('div');
        label.className = 'layer-label';
        label.textContent = layer.name;
        label.style.position = 'absolute';
        label.style.left = `${(layerIndex + 1) * layerSpacing}px`;
        label.style.top = '10px';
        label.style.transform = 'translateX(-50%)';
        label.style.fontWeight = 'bold';
        container.appendChild(label);

        for (let i = 0; i < layer.nodes; i++) {
            const node = document.createElement('div');
            node.className = 'node';
            node.style.position = 'absolute';
            node.style.width = `${nodeRadius * 2}px`;
            node.style.height = `${nodeRadius * 2}px`;
            node.style.borderRadius = '50%';
            node.style.backgroundColor = layer.color;
            node.style.zIndex = '2';
            
            const x = (layerIndex + 1) * layerSpacing;
            const y = (height / (layer.nodes + 1)) * (i + 1);
            
            node.style.left = `${x - nodeRadius}px`;
            node.style.top = `${y - nodeRadius}px`;
            
            container.appendChild(node);

            // Create connections to next layer
            if (layerIndex < layers.length - 1) {
                for (let j = 0; j < layers[layerIndex + 1].nodes; j++) {
                    const connection = document.createElement('div');
                    connection.className = 'connection';
                    connection.style.position = 'absolute';
                    connection.style.height = '2px';
                    connection.style.backgroundColor = '#bdc3c7';
                    connection.style.transformOrigin = '0 0';
                    connection.style.zIndex = '1';
                    
                    const x2 = (layerIndex + 2) * layerSpacing;
                    const y2 = (height / (layers[layerIndex + 1].nodes + 1)) * (j + 1);
                    
                    const length = Math.sqrt(Math.pow(x2 - x, 2) + Math.pow(y2 - y, 2));
                    const angle = Math.atan2(y2 - y, x2 - x) * 180 / Math.PI;
                    
                    connection.style.width = `${length}px`;
                    connection.style.left = `${x}px`;
                    connection.style.top = `${y}px`;
                    connection.style.transform = `rotate(${angle}deg)`;
                    
                    container.appendChild(connection);
                }
            }
        }
    });
    
    // Animation timeline
    const timeline = anime.timeline({
        loop: true,
        duration: 5000,
        easing: 'linear'
    });

    // Animate nodes appearing
    timeline.add({
        targets: '.node',
        scale: [0, 1],
        opacity: [0, 1],
        duration: 1000,
        easing: 'easeOutElastic(1, .5)',
        delay: anime.stagger(100)
    });

    // Animate connections appearing
    timeline.add({
        targets: '.connection',
        opacity: [0, 0.5],
        scaleX: [0, 1],
        duration: 1000,
        easing: 'easeOutQuad',
        delay: anime.stagger(50)
    }, '-=500');  // Start before nodes finish appearing

    // Keep everything visible
    timeline.add({
        duration: 2000  // Adjust this to control how long everything stays visible
    });

    // Animate connections disappearing
    timeline.add({
        targets: '.connection',
        opacity: 0,
        scaleX: 0,
        duration: 500,
        easing: 'easeInQuad',
        delay: anime.stagger(25, {from: 'center'})
    });

    // Animate nodes disappearing
    timeline.add({
        targets: '.node',
        scale: 0,
        opacity: 0,
        duration: 500,
        easing: 'easeInQuad',
        delay: anime.stagger(50, {from: 'last'})
    }, '-=250');  // Start before connections finish disappearing
}

// Call the function when the page loads
window.addEventListener('load', createNeuralNetworkAnimation);
</script>


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
    mymap = L.map('mapid', {
        worldCopyJump: false,
        maxBounds: [[-90, -180], [90, 180]],
        minZoom: 2
    }).setView([20, 0], 2);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        noWrap: true
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

function createStateMarkers(states) {
    Object.entries(states).forEach(([state, stateData]) => {
        if (stateCenters[state]) {
            const stateMarker = L.circleMarker(stateCenters[state], {
                radius: Math.sqrt(stateData.count) * 2,
                fillColor: "green",
                color: "#000",
                weight: 1,
                opacity: 1,
                fillOpacity: 0.8
            }).addTo(mymap);

            stateMarker.bindPopup(`${state}: ${stateData.count} strains`);
            stateMarker.on('click', (e) => {
                e.originalEvent.stopPropagation();
                updateStrainList(
                    Array.from(stateData.strains).map(s => JSON.parse(s)),
                    `Strains in ${state}`
                );
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

    // Add title to the scatterplot
    svg.append("text")
        .attr("x", width / 2)
        .attr("y", margin.top / 2)
        .attr("text-anchor", "middle")
        .style("font-size", "20px")
        .style("font-weight", "bold")
        .text("MDS of HCMV Genomes");

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

// Initialize everything
initMap();
loadData();
</script>