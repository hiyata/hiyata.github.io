---
layout: post
title:  "Migration Patterns Behind HCMV Diversity"
date:   2024-08-01 13:00:00 -0400
categories: jekyll update
excerpt: "Can ancient human migration explain the geographic diversity of HCMV, and does that shared history help explain why some people get sick from infection while most never notice it at all?"
---

<p>
Human betaherpesvirus 5 (HHV-5), better known as human cytomegalovirus (HCMV), is one of the
most widespread and host-specific viruses we know. Herpesviruses are thought to have co-evolved
with their hosts across hundreds of millions of years<sup><a href="#ref-1">1</a></sup>, and as a
result they tend to be tightly adapted to a single host species, rarely infecting anything
outside their normal range. HCMV is also extremely common: seroprevalence in adults runs as high
as 80% worldwide<sup><a href="#ref-2">2</a></sup>. Most infected adults never notice, the virus
simply establishes life-long residency in their cells and stays quiet.
</p>

<p>
That long, quiet coexistence is the interesting part. Most of the pathogens that make headlines,
SARS-CoV-2, Ebola, HIV, are zoonotic in origin: they jumped into humans relatively recently, and
spillover events like that tend to be the source of the deadliest outbreaks, the host hasn't had
time to adapt. HCMV is the opposite case. It has been shaped by, and shaping, human hosts for a
very long time, and that history shows up directly in its genome. Recent work on HCMV strain
collections has found that strains cluster geographically, sequences sampled from southeast
Africa, for instance, sit apart from the rest of the dataset as one of its most distinct groups.
That's the pattern this post digs into.
</p>

<h2>What 330 HCMV genomes look like in strain-space</h2>
<p>
Below is a multidimensional scaling (MDS) projection of 330 publicly available HCMV genomes,
built from pairwise genomic distance and reduced to two components so the overall structure is
visible at a glance. Each point is one strain, colored by the continent it was sampled from, and
you can hover any point for its strain name and country of origin.
</p>

<div class="mds-figure">
  <div id="scatterPlot" style="height: 600px; width: 100%;"></div>
</div>
<p class="mds-figure-note">
  n = 330 strains &middot; Europe (266) and Africa (36, mostly Zambia and Kenya) make up the bulk
  of publicly available sequence, which is itself a sampling bias worth keeping in mind, but the
  African cluster's separation from the European core holds up regardless.
</p>

<p>
The African strains, Zambian sequences especially, sit toward the outer edge of the projection
rather than blending into the larger Eurasian cluster. That's consistent with deeper genomic
divergence, which is exactly what you'd expect if HCMV has been differentiating alongside human
populations since long before recent global travel started mixing everything back together.
</p>

<h2>A viral map that mirrors a human one</h2>
<p>
If HCMV diversified as it traveled with us, its genomic map should echo our own migration map,
at least roughly. Human genetic diversity carries a well-documented signature of the
out-of-Africa expansion: populations that migrated furthest from the origin generally show
reduced diversity relative to those that stayed closer to it, a serial founder-effect pattern
repeated at every step of the journey. Immune-related genes are no exception, historic
migration and the pathogens encountered along the way have measurably shaped how human immune
variation is distributed across populations today<sup><a href="#ref-4">4</a></sup>.
</p>

<figure>
  <img src="{{ '/assets/images/migration_patterns_PMID_31786023.webp' | relative_url }}" alt="Map of early human migration out of Africa, showing approximate routes and timing in thousands of years ago, including introgression events with Neanderthals and Denisovans">
  <figcaption>Approximate routes and timing of early human migration out of Africa, with Neanderthal and Denisovan introgression events marked. From Domínguez-Andrés &amp; Netea, 2019<sup><a href="#ref-4">4</a></sup>.</figcaption>
</figure>

<figure>
  <img src="{{ '/assets/images/world_map_of_y-dna_haplogroups.webp' | relative_url }}" alt="World map of Y-DNA haplogroups showing dominant paternal lineages in native populations and their proposed migration routes">
  <figcaption>Y-DNA haplogroup distribution and proposed migration routes, a complementary view of the same population movements a host-adapted virus would have traveled alongside.</figcaption>
</figure>

<p>
Line the two maps up against the HCMV projection above and the parallel is hard to miss: the
same broad strokes, an African origin, a long Eurasian spread, more isolated founder populations
at the far ends of the migration routes, show up in both the human genetic record and, more
faintly so far, in HCMV's.
</p>

<h2>An open question worth testing</h2>
<p>
Primary HCMV infection is usually silent in healthy adults, but not always, some people develop
mononucleosis<sup><a href="#ref-3">3</a></sup>, and we still don't have a good explanation for why.
One hypothesis this pattern suggests: HCMV strains that co-evolved with a given human population
over a long stretch of shared history may simply be better tolerated by descendants of that
population than a strain introduced more recently from elsewhere, the same logic that makes a
pathogen most dangerous right after it jumps into a new host applies, in a milder form, to
mismatches between a well-adapted virus and an unfamiliar host population. That's a hypothesis,
not a finding, the strain-clustering pattern above is suggestive, not proof, but it's a concrete,
testable direction: pairing strain phylogeography with host ancestry and clinical outcome data
is the natural next step.
</p>

<h2>References</h2>
<ol>
  <li id="ref-1">Davison AJ. Evolution of the herpesviruses. <em>Vet Microbiol.</em> 2002 Apr 22;86(1-2):69-88. doi: <a href="https://doi.org/10.1016/s0378-1135(01)00492-8" target="_blank" rel="noopener">10.1016/s0378-1135(01)00492-8</a>. PMID: <a href="https://pubmed.ncbi.nlm.nih.gov/11888691/" target="_blank" rel="noopener">11888691</a>.</li>
  <li id="ref-2">Zuhair M, Smit GSA, Wallis G, et al. Estimation of the worldwide seroprevalence of cytomegalovirus: A systematic review and meta-analysis. <em>Rev Med Virol.</em> 2019;29:e2034. doi: <a href="https://doi.org/10.1002/rmv.2034" target="_blank" rel="noopener">10.1002/rmv.2034</a>.</li>
  <li id="ref-3">Mayo Clinic Staff. Mononucleosis: Symptoms and causes. <em>Mayo Clinic.</em> <a href="https://www.mayoclinic.org/diseases-conditions/cmv/symptoms-causes/syc-20355358" target="_blank" rel="noopener">mayoclinic.org</a>.</li>
  <li id="ref-4">Domínguez-Andrés J, Netea MG. Impact of Historic Migrations and Evolutionary Processes on Human Immunity. <em>Trends Immunol.</em> 2019 Dec;40(12):1105-1119. PMID: <a href="https://pubmed.ncbi.nlm.nih.gov/31786023/" target="_blank" rel="noopener">31786023</a>.</li>
</ol>

<script src="https://cdnjs.cloudflare.com/ajax/libs/PapaParse/5.3.0/papaparse.min.js"></script>
<script src="https://d3js.org/d3.v7.min.js"></script>

<style>
  .mds-figure {
    border: 1px solid var(--border);
    border-radius: var(--radius-md);
    background: var(--surface);
    padding: 1rem;
    margin: 1.5rem 0 0.75rem;
  }
  .mds-figure-note {
    font-family: var(--mono);
    font-size: 0.78em;
    color: var(--ink-faint);
    margin: 0 0 1.5rem;
  }
  #scatterPlot .domain,
  #scatterPlot .tick line {
    stroke: var(--border-strong);
  }
  #scatterPlot .tick text,
  #scatterPlot .axis-label,
  #scatterPlot text {
    fill: var(--ink-soft);
  }
  #scatterPlot .chart-title {
    fill: var(--ink);
  }
</style>

<script>

// Function to process CSV data
function processData(results) {
    const data = results.data.filter(row => row.Continent && row.Country && row.Strain && row.ID && row.Component1 && row.Component2);
    return { data };
}

// Function to create the MDS scatter plot
function createScatterPlot(data) {
    const scatterPlot = document.getElementById('scatterPlot');
    const width = scatterPlot.clientWidth;
    const height = scatterPlot.clientHeight;
    const margin = { top: 60, right: 140, bottom: 80, left: 80 };
    const plotWidth = width - margin.left - margin.right;
    const plotHeight = height - margin.top - margin.bottom;

    const rootStyles = getComputedStyle(document.documentElement);
    const surfaceColor = rootStyles.getPropertyValue('--surface').trim() || '#ffffff';
    const borderColor = rootStyles.getPropertyValue('--border').trim() || '#e2dbca';

    const svg = d3.select('#scatterPlot')
        .append('svg')
        .attr('width', width)
        .attr('height', height);

    // Add title to the scatterplot
    svg.append("text")
        .attr("class", "chart-title")
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
        .attr('text-anchor', 'middle')
        .attr('font-size', '16px')
        .text('Component 1');

    g.append('text')
        .attr('class', 'axis-label')
        .attr('transform', 'rotate(-90)')
        .attr('y', -60)
        .attr('x', -plotHeight / 2)
        .attr('dy', '1em')
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
            .attr('opacity', 0.3);
    });

    const points = g.selectAll('.point')
        .data(filteredData)
        .enter().append('circle')
        .attr('class', 'point')
        .attr('r', 4)
        .attr('cx', d => x(parseFloat(d.Component1)))
        .attr('cy', d => y(parseFloat(d.Component2)))
        .attr('fill', d => color(d.Continent))
        .attr('stroke', surfaceColor)
        .attr('stroke-width', 1)
        .attr('opacity', 0.8);

    // Add legend
    svg.append('rect')
        .attr('x', width - margin.right + 10)
        .attr('y', margin.top)
        .attr('width', margin.right - 20)
        .attr('height', 110)
        .attr('fill', surfaceColor)
        .attr('stroke', borderColor);

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
    Papa.parse('{{ "/assets/csv_files/hcmv_strains.csv" | relative_url }}', {
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
