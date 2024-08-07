---
layout: default
title:  "Migration Patterns Behind HCMV Diversity"
date:   2024-08-01 13:00:00 -0400
categories: jekyll update
excerpt: "Can ancient migration patterns explain the geographic diversity of HCMV and help us better understand varying tolerances to herpesvirus infection?"
---

<h2>Migration Patterns Behind HCMV Diversity</h2>

<p>Viruses are obligate, intracellular parasites and are most known for their role in pathogenesis. Viruses come in many flavors, from DNA to RNA, single-stranded or double-stranded, and circular or linear. They are thought to have been some of the first life-forms to evolve on Earth and drivers of evolution in other forms of life.</p>

<p>Some viruses have evolved adjacently with their hosts for millions of years, such as human cytomegalovirus. The result of this coexistence is highly specialized viruses tailored to thrive in human hosts without causing pathogenesis.</p>

<div id="scatterPlot" class="animate" style="height: 600px; width: 100%; margin-bottom: 20px;"></div>

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
    Papa.parse('/assets/csv_files/hcmv_strains.csv', {
        download: true,
        header: true,
        complete: function(results) {
            let globalData = processData(results);
            createScatterPlot(globalData.data);
        }
    });
}

// Call loadData when the page is loaded
document.addEventListener('DOMContentLoaded', loadData);
</script>

<img src="/assets/images/migration_patterns_PMID_31786023.jpg" alt="Migration Patterns">

<p>test test test</p>

<img src="/assets/images/world_map_of_y-dna_haplogroups.jpg" alt="World Map of Y-DNA Haplogroups">