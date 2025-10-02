---
layout: page
title: HCMV Multi-Omic Analysis
permalink: /hcmv-analysis/
---

<div class="scientific-dashboard">
    <!-- Header Section -->
    <header class="dashboard-header">
        <h1>HCMV Multi-Omic Analysis Dashboard</h1>
        <div class="header-metadata">
            <p class="description">
                Alignment of all omic data in this study clustered by temporal classes and sorted by genome position.
                All rows are scaled independently. For all columns, blank cells denote missing data.

                <br><br>
                <strong>A) Temporal transcriptomics:</strong> Temporal changes in transcript abundances over hours post-infection.
                <br><br>
                <strong>B) Virion analysis:</strong> Single condition showing localization of each protein. Colored by localization, abundance shown in hover.
                <br><br>
                <strong>C) Temporal proteomics (96h):</strong> Protein abundances across multiple time points.
                <br><br>
                <strong>D) Temporal proteomics (120h):</strong> Protein abundances across multiple time points.
                <br><br>
                <strong>E) Spatial proteomics:</strong> Localization patterns at multiple time points.
                <br><br>
                <strong>F) Interactomics:</strong> Binary/categorical interaction data across conditions.
                <br><br>
                <strong>G) Phenomics:</strong> Growth defect phenotypes across conditions.
            </p>
            <div class="dataset-info">
                <span class="dataset-metric">
                    <i class="fas fa-dna"></i>
                    Total Genes: <span id="geneCount">0</span>
                </span>
                <span class="dataset-metric">
                    <i class="fas fa-clock"></i>
                    Time Points: Variable
                </span>
                <span class="dataset-metric">
                    <i class="fas fa-microscope"></i>
                    Data Types: 7
                </span>
            </div>
        </div>
    </header>

    <!-- Navigation Tabs -->
    <div class="analysis-tabs">
        <button class="tab-button active" data-tab="A">A. Temporal Transcriptomics</button>
        <button class="tab-button" data-tab="B">B. Virion Analysis</button>
        <button class="tab-button" data-tab="C">C. Temporal Proteomics (96h)</button>
        <button class="tab-button" data-tab="D">D. Temporal Proteomics (120h)</button>
        <button class="tab-button" data-tab="E">E. Spatial Proteomics</button>
        <button class="tab-button" data-tab="F">F. Interactomics</button>
        <button class="tab-button" data-tab="G">G. Phenomics</button>
    </div>

    <!-- Control Panel -->
    <div class="control-panel">
        <div class="search-section">
            <input type="text" id="geneSearch" placeholder="Search genes..." class="search-input">
            <select id="temporalClassSelect" class="data-select">
                <option value="all">All Temporal Classes</option>
            </select>
        </div>
        <div class="visualization-controls">
            <div class="view-toggle">
                <button id="heatmapView" class="view-btn active" title="Heatmap View">
                    <i class="fas fa-th"></i> Heatmap
                </button>
                <button id="lineView" class="view-btn" title="Line Plot View">
                    <i class="fas fa-chart-line"></i> Line Plot
                </button>
                <button id="tableView" class="view-btn" title="Table View">
                    <i class="fas fa-table"></i> Table
                </button>
            </div>
             <button id="toggleRelative" class="download-btn" style="background: #8e44ad;" title="Toggle Relative Abundance">
                <i class="fas fa-exchange-alt"></i> Use Relative Abundance
            </button>
            <button id="toggleIncomplete" class="download-btn" style="background: #e67e22;" title="Toggle Hide Incomplete">
                <i class="fas fa-filter"></i> Hide Incomplete
            </button>
            <button id="downloadData" class="download-btn" title="Download Data">
                <i class="fas fa-download"></i> Export Data
            </button>
        </div>
    </div>

    <!-- Main Content Area -->
    <div class="main-content">
        <!-- Visualization Area -->
        <div class="visualization-area">
            <div id="dataDescription" class="data-description"></div>
             <div id="loadingIndicator" class="loading-indicator">Loading Data...</div>
            <div id="mainVisualization" class="visualization-container"></div>
            <div id="legendContainer" class="legend-container"></div>
            <div id="errorMessage" class="error-message" style="display: none;"></div>
        </div>

        <!-- Details Panel -->
        <aside class="details-panel">
            <div id="geneDetails" class="gene-details">
                <h3>Gene Details</h3>
                <div class="details-content">
                    Select a gene to view details
                </div>
            </div>
            <div class="statistics-panel">
                <h3>Statistics</h3>
                <div id="statsContent" class="stats-content"></div>
            </div>
        </aside>
    </div>
</div>

<style>
    :root {
    --primary-color: #2c3e50;
    --secondary-color: #3498db;
    --accent-color: #e74c3c;
    --success-color: #2ecc71;
    --warning-color: #f1c40f;
    --background-color: #f5f6fa;
    --card-background: #ffffff;
    --text-color: #2c3e50;
    --border-color: #dfe6e9;
    --shadow-color: rgba(0, 0, 0, 0.1);
    --transition-speed: 0.3s;
    --legend-font-size: 0.9rem;
    --legend-padding: 10px;
}

.scientific-dashboard {
    max-width: 1600px;
    margin: 0 auto;
    padding: 20px;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    color: var(--text-color);
}

.dashboard-header {
    background: var(--card-background);
    padding: 2rem;
    border-radius: 8px;
    box-shadow: 0 2px 4px var(--shadow-color);
    margin-bottom: 2rem;
}

.dashboard-header h1 {
    color: var(--primary-color);
    font-size: 2.2rem;
    margin: 0 0 1rem 0;
    font-weight: 600;
}

.header-metadata {
    display: grid;
    gap: 1rem;
}

.description {
    font-size: 1rem;
    color: #666;
    margin: 0;
    line-height: 1.5;
}

.dataset-info {
    display: flex;
    gap: 2rem;
    font-size: 0.9rem;
}

.dataset-metric {
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.dataset-metric i {
    color: var(--secondary-color);
}

.analysis-tabs {
    display: flex;
    gap: 0.5rem;
    margin-bottom: 1.5rem;
    overflow-x: auto;
    padding-bottom: 0.5rem;
}

.tab-button {
    padding: 0.8rem 1.2rem;
    border: none;
    background: var(--card-background);
    color: var(--text-color);
    border-radius: 6px;
    cursor: pointer;
    transition: all var(--transition-speed);
    white-space: nowrap;
    font-weight: 500;
}

.tab-button.active {
    background: var(--secondary-color);
    color: white;
}

.control-panel {
    display: grid;
    grid-template-columns: 1fr auto;
    gap: 1rem;
    background: var(--card-background);
    padding: 1rem;
    border-radius: 8px;
    box-shadow: 0 2px 4px var(--shadow-color);
    margin-bottom: 1.5rem;
}

.search-section {
    display: flex;
    gap: 1rem;
}

.search-input {
    padding: 0.8rem 1rem;
    border: 1px solid var(--border-color);
    border-radius: 6px;
    font-size: 1rem;
    min-width: 300px;
}

.data-select {
    padding: 0.8rem;
    border: 1px solid var(--border-color);
    border-radius: 6px;
    background: white;
}

.visualization-controls {
    display: flex;
    gap: 1rem;
    align-items: center;
}

.view-toggle {
    display: flex;
    border: 1px solid var(--border-color);
    border-radius: 6px;
    overflow: hidden;
}

.view-btn {
    padding: 0.8rem 1.2rem;
    border: none;
    background: white;
    cursor: pointer;
    transition: all var(--transition-speed);
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.view-btn.active {
    background: var(--secondary-color);
    color: white;
}

.download-btn {
    padding: 0.8rem 1.2rem;
    background: var(--success-color);
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    transition: all var(--transition-speed);
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.main-content {
    display: grid;
    grid-template-columns: 250px 1fr 300px;
    gap: 1.5rem;
    margin-top: 1.5rem;
}

.filters-panel {
    background: var(--card-background);
    padding: 1.5rem;
    border-radius: 8px;
    box-shadow: 0 2px 4px var(--shadow-color);
}

.filter-section h3 {
    margin: 0 0 1rem 0;
    font-size: 1.1rem;
    color: var(--primary-color);
}

.filter-group {
    margin-bottom: 1.5rem;
}

.filter-group h4 {
    margin: 0 0 0.8rem 0;
    font-size: 0.9rem;
    color: #666;
}

.range-slider {
    margin-top: 1rem;
}

.visualization-area {
    background: var(--card-background);
    padding: 1.5rem;
    border-radius: 8px;
    box-shadow: 0 2px 4px var(--shadow-color);
    display: flex;
    flex-direction: column;
    gap: 1rem;
     position: relative; /* For loading indicator */
}

.data-description {
    padding: 1rem;
    background: #f8f9fa;
    border-radius: 6px;
    font-size: 0.9rem;
    line-height: 1.5;
}

.visualization-container {
    flex-grow: 1;
    min-height: 500px;
    overflow-x: auto;
}

.legend-container {
    padding: var(--legend-padding);
    background: #f8f9fa;
    border-radius: 6px;
    font-size: var(--legend-font-size);
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
}

.details-panel {
    background: var(--card-background);
    padding: 1.5rem;
    border-radius: 8px;
    box-shadow: 0 2px 4px var(--shadow-color);
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
}

.gene-details h3,
.statistics-panel h3 {
    margin: 0 0 1rem 0;
    font-size: 1.1rem;
    color: var(--primary-color);
}

.details-content,
.stats-content {
    font-size: 0.9rem;
    line-height: 1.5;
}

.data-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.9rem;
}

.data-table th,
.data-table td {
    border: 1px solid var(--border-color);
    padding: 8px;
    text-align: center;
}

.data-table th {
    background: var(--secondary-color);
    color: white;
}

.data-table tr:nth-child(even) {
    background: #f2f2f2;
}

.error-message {
    padding: 1rem;
    background: var(--warning-color);
    color: white;
    border-radius: 6px;
    margin-bottom: 1rem;
    font-weight: bold;
}

/* Loading indicator */
.loading-indicator {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 1.2em;
    color: #777;
    display: none; /* Initially hidden */
}

.loading-indicator.show {
    display: block;
}


@media (max-width: 1400px) {
    .main-content {
        grid-template-columns: 1fr;
    }

    .filters-panel {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1rem;
    }
}

@media (max-width: 768px) {
    .control-panel {
        grid-template-columns: 1fr;
    }

    .search-section {
        flex-direction: column;
    }

    .visualization-controls {
        justify-content: space-between;
    }

    .search-input {
        min-width: auto;
    }
}
</style>

<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/noUiSlider/15.7.1/nouislider.min.js"></script>
<link href="https://cdnjs.cloudflare.com/ajax/libs/noUiSlider/15.7.1/nouislider.min.css" rel="stylesheet"/>
<script src="https://kit.fontawesome.com/a076d05399.js"></script>

<script>
  const colorPalettes = {
        localization: {
            'Lysosome': '#1f77b4',
            'Golgi': '#ff7f0e',
            'Peroxisome': '#2ca02c',
            'ER': '#d62728',
            'Nucleus': '#9467bd',
            'Mitochondria': '#8c564b',
            'Undefined': '#7f7f7f',
            'Tegument': '#e377c2',
            'Capsid': '#bcbd22',
            'Envelope': '#17becf',
            'Other': '#8c564b'
        },
        hcpi: {
            '1': '#2ca02c',
            '0': '#d62728'
        },
        phenomics_p1_p2: {
            'Y': '#2ca02c',
            'N': '#d62728'
        },
        temporalClass: {
            'Early': '#1f77b4',
            'Mid': '#ff7f0e',
            'Late': '#2ca02c',
            'Undefined': '#7f7f7f'
        }
    };

    const dataCategories = {
        A: {
            description: 'A) Temporal transcriptomics: Temporal changes in transcript abundances over hours.',
            title: 'A. Temporal Transcriptomics',
            columns: null,
            dataType: 'numeric',
            file: '/assets/tables/A_Temporal_Transcriptomics.csv'
        },
        B: {
            description: 'B) Virion Analysis: Single condition showing protein localization, colored by localization.',
            title: 'B. Virion Analysis',
            columns: null,
            dataType: 'mixed',
            file: '/assets/tables/B_Viral_Proteins.csv'
        },
        C: {
            description: 'C) Temporal Proteomics (96h): Protein abundances across multiple time points.',
            title: 'C. Temporal Proteomics (96h)',
            columns: null,
            dataType: 'numeric',
            file: '/assets/tables/C_Temporal_Proteomics_96.csv'
        },
        D: {
            description: 'D) Temporal Proteomics (120h): Protein abundances across multiple time points.',
            title: 'D. Temporal Proteomics (120h)',
            columns: null,
            dataType: 'numeric',
            file: '/assets/tables/D_Temporal_Proteomics_120_NoSuffix.csv'
        },
        E: {
            description: 'E) Spatial Proteomics: Localization patterns over time points.',
            title: 'E. Spatial Proteomics',
            columns: null,
            dataType: 'categorical',
            file: '/assets/tables/E_Spatial_Proteomics_NoSuffix.csv'
        },
        F: {
            description: 'F) Interactomics: Binary/categorical interaction data across conditions.',
            title: 'F. Interactomics',
            columns: null,
            dataType: 'binary',
            file: '/assets/tables/F_Interactomics.csv'
        },
        G: {
            description: 'G. Phenomics: Growth defect phenotypes across conditions.',
            title: 'G. Phenomics',
            columns: null,
            dataType: 'categorical',
            file: '/assets/tables/G_Phenomics.csv'
        }
    };

    let rawData = {};
    let processedData = {};
    let currentTab = 'A';
    let currentView = 'heatmap';
    let allGeneNames = [];
    let hideIncomplete = false;
    let useRelative = false;
    const numericColorScale = 'Viridis';
    const debug = false;

    document.addEventListener('DOMContentLoaded', initializeDashboard);

    async function initializeDashboard() {
        showLoading(true);
        try {
            await loadAllData();
            setupEventListeners();
            setupFilters();
            updateVisualization();
            updateDashboardMetrics();
        } catch (error) {
            handleError(error);
        } finally {
           showLoading(false);
        }
    }

    async function loadAllData() {
        const fetchPromises = Object.keys(dataCategories).map(cat => {
            return fetchCSV(dataCategories[cat].file)
                .then(csvData => {
                    rawData[cat] = csvData;
                    const headers = Object.keys(csvData[0] || {});
                    const metadataFields = ['Gene', 'Temporal_Class', 'Loc.', 'Abd.', 'HCIP', 'P1', 'P2'];
                    const dataCols = headers.filter(h => !metadataFields.includes(h));
                    dataCategories[cat].columns = dataCols;
                    processedData[cat] = processDataByCategory(csvData, dataCols, dataCategories[cat].dataType);
                })
                .catch(error => {
                    handleError(`Error loading ${dataCategories[cat].file}: ${error}`);
                    throw error;
                });
        });
        await Promise.all(fetchPromises);
        allGeneNames = Array.from(new Set(Object.values(rawData).flat().map(d => d.Gene))).sort();
    }

    async function fetchCSV(url) {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`Failed to fetch ${url}: ${response.status} ${response.statusText}`);
        }
        const csvText = await response.text();
        return parseCSV(csvText);
    }

    function parseCSV(csvText) {
        const lines = csvText.split('\n').filter(line => line.trim() !== '');
        if (lines.length === 0) return [];
        const headers = lines[0].split(',').map(h => h.trim());
        const data = lines.slice(1).map(line => {
            const values = line.split(',').map(v=>v.trim());
            return headers.reduce((obj,header,index)=>{
                obj[header] = values[index]||'';
                return obj;
            },{});
        });
        return data;
    }

    function processDataByCategory(data, columns, dataType) {
        return data.map(row => {
            const loc = row['Loc.'] && row['Loc.'].trim() !== '' ? row['Loc.'] : 'Undefined';
            const abd = row['Abd.'] || '';
            const hcpi = row['HCIP'] || '';
            const p1 = row['P1'] || '';
            const p2 = row['P2'] || '';
            const temporalClass = row['Temporal_Class'] && row['Temporal_Class'].trim() !== '' ? row['Temporal_Class'] : 'Undefined';

            let values = columns.map(col => {
                const val = row[col] || '';
                if (['categorical', 'binary', 'mixed'].includes(dataType)) {
                    return val.trim() === '' ? 'Undefined' : val;
                }
                return val;
            });

            return {
                gene: row.Gene,
                values: values,
                metadata: {
                    localization: loc,
                    abundance: abd,
                    hcpi: hcpi,
                    p1: p1,
                    p2: p2,
                    temporalClass: temporalClass
                },
                dataType: dataType
            };
        });
    }

    function updateDashboardMetrics() {
        const geneCountEl = document.getElementById('geneCount');
        if (geneCountEl) geneCountEl.textContent = allGeneNames.length;
    }

    function isTimeColumn(col) {
        return /\d+h$/.test(col);
    }

    function parseHour(col) {
        const match = col.match(/(\d+)h$/);
        return match ? parseInt(match[1], 10) : null;
    }

    function getPlotColumns(columns) {
        const timeCols = columns.filter(isTimeColumn);
        if (timeCols.length === columns.length) {
            return timeCols.sort((a, b) => parseHour(a) - parseHour(b));
        }
        return columns;
    }

    function applyRelativeAbundance(data) {
        const currentType = dataCategories[currentTab].dataType;
        if (!useRelative || (currentType !== 'numeric' && currentType !== 'mixed')) return data;

        return data.map(d => {
            const nums = d.values.map(v => parseFloat(v));
            const validNums = nums.filter(n => !isNaN(n));
            if (validNums.length === 0) return d;
            const maxVal = Math.max(...validNums);
            if (maxVal > 0) {
                const newValues = d.values.map(val => {
                    const x = parseFloat(val);
                    return isNaN(x) ? 'Undefined' : (x / maxVal).toString();
                });
                return { ...d, values: newValues };
            }
            return d;
        });
    }


    function filterData() {
        let filteredData = processedData[currentTab];
        filteredData = applyRelativeAbundance(filteredData);

        const temporalClassSelect = document.getElementById('temporalClassSelect');
        if (temporalClassSelect && temporalClassSelect.value !== 'all') {
            filteredData = filteredData.filter(d => d.metadata.temporalClass === temporalClassSelect.value);
        }

        const dataType = dataCategories[currentTab].dataType;
        const slider = document.getElementById('abundanceSlider');
        if ((dataType === 'numeric' || dataType === 'mixed') && slider && slider.noUiSlider) {
            const [min, max] = slider.noUiSlider.get().map(parseFloat);
            filteredData = filteredData.filter(d => {
                return d.values.some(v => {
                    const val = parseFloat(v);
                    return !isNaN(val) && val >= min && val <= max;
                });
            });
        }

        const searchTerm = (document.getElementById('geneSearch').value || '').toLowerCase();
        if (searchTerm) {
            filteredData = filteredData.filter(d => d.gene.toLowerCase().includes(searchTerm));
        }

        if (hideIncomplete) {
            filteredData = filteredData.filter(d => {
                return !d.values.some(v => v === 'Undefined' || v === '' || v === 'N/A');
            });
        }

        return filteredData;
    }

    function filterDataForDisplay() {
        return filterData();
    }

    function createHeatmap(data, columns) {
    const sortedCols = getPlotColumns(columns);
    const colIndices = sortedCols.map(c=>columns.indexOf(c));

    const geneIndex = {};
    allGeneNames.forEach((g,i)=>geneIndex[g]=i);
    const zValues = Array.from({length:allGeneNames.length},()=>Array(columns.length).fill(null));

    data.forEach(d=>{
        const idx = geneIndex[d.gene];
        d.values.forEach((val,i)=>{
            const num = parseFloat(val);
            zValues[idx][i] = isNaN(num)?null:num;
        });
    });

    const reorderedZ = zValues.map(row=>colIndices.map(i=>row[i]));
    const plotData=[{
        z: reorderedZ,
        x: sortedCols,
        y: allGeneNames,
        type:'heatmap',
        colorscale:numericColorScale,
        hoverongaps:false,
        colorbar:{title:'Abundance',titleside:'right'},
        hovertemplate:'Gene: %{y}<br>%{x}: %{z}<extra></extra>'
    }];

    const layout={
        title:dataCategories[currentTab].title,
        xaxis:{title:'Time (hours)',side:'bottom',automargin:true},
        yaxis:{title:'Genes',automargin:true},
        margin:{t:50,r:50,b:150,l:200},
        height:800,
        hovermode:'closest'
    };

    Plotly.newPlot('mainVisualization',plotData,layout,{responsive:true});
}

function createCategoricalHeatmap(data, columns, categoryType) {
    const sortedCols = getPlotColumns(columns);
    const colIndices = sortedCols.map(c=>columns.indexOf(c));

    const geneIndex={};
    allGeneNames.forEach((g,i)=>geneIndex[g]=i);
    const zValues = Array.from({length:allGeneNames.length},()=>Array(columns.length).fill('Undefined'));
    data.forEach(d=>{
        const idx=geneIndex[d.gene];
        d.values.forEach((val,i)=>{
            zValues[idx][i]=val||'Undefined';
        });
    });

    const reorderedZ = zValues.map(row=>colIndices.map(i=>row[i]));

    const uniqueCategories=Array.from(new Set(reorderedZ.flat())).sort();
    let palette = colorPalettes.localization;
    if(categoryType==='hcpi') palette=colorPalettes.hcpi;
    else if(categoryType==='phenomics') palette=colorPalettes.phenomics_p1_p2;

    const colorScale = uniqueCategories.map(cat=>palette[cat]||'#7f7f7f');
    const zNumeric = reorderedZ.map(row=>row.map(val=>uniqueCategories.indexOf(val)));
    const plotlyColorscale=uniqueCategories.map((cat,i)=>[i/(uniqueCategories.length-1),colorScale[i]]);

    const plotData=[{
        z:zNumeric,
        x:sortedCols,
        y:allGeneNames,
        type:'heatmap',
        colorscale:plotlyColorscale,
        showscale:false,
        hoverongaps:false,
        text:reorderedZ,
        hovertemplate:'Gene: %{y}<br>%{x}: %{text}<extra></extra>'
    }];

    const layout={
        title:dataCategories[currentTab].title,
        xaxis:{title:'Time (hours)',automargin:true},
        yaxis:{title:'Genes',automargin:true},
        margin:{t:50,r:50,b:150,l:200},
        height:800,
        hovermode:'closest'
    };

     Plotly.newPlot('mainVisualization',plotData,layout,{responsive:true}).then(()=>{
          createLegend(uniqueCategories,colorScale);
     });
}

    function createLinePlot(data, columns) {
        const currentType = dataCategories[currentTab].dataType;
        if (currentType !== 'numeric' && currentType !== 'mixed') {
            createDataTable(data, columns);
            return;
        }

        const sortedCols = getPlotColumns(columns);
        const times = sortedCols.map(c => isTimeColumn(c) ? parseHour(c) : c);
        const numericTimes = times.every(t => typeof t === 'number');
        const xValues = numericTimes ? times : sortedCols;

        const traces = data.map(d => {
            const yVals = d.values.map(v => parseFloat(v));
            const reorderedY = sortedCols.map(c => {
                const originalIndex = columns.indexOf(c);
                return parseFloat(d.values[originalIndex]);
            });

            return {
                x: xValues,
                y: reorderedY,
                name: d.gene,
                mode: 'lines+markers',
                type: 'scatter',
                hovertemplate: 'Gene: ' + d.gene + '<br>%{x}: %{y}<extra></extra>'
            };
        });

        const xLabel = numericTimes ?'Time (hours)' : 'Conditions';
        const yLabel = 'Abundance';

        const layout = {
            title: dataCategories[currentTab].title,
            xaxis: { title: xLabel, automargin: true },
            yaxis: { title: yLabel, autorange: true },
            margin: { t: 50, r: 50, b: 100, l: 100 },
            height: 800,
            hovermode: 'closest',
            showlegend: true
        };

        Plotly.newPlot('mainVisualization', traces, layout, { responsive: true });
    }

    function createDataTable(data, columns) {
        const tableContainer = document.getElementById('mainVisualization');
        if (!tableContainer) return;
        tableContainer.innerHTML = '';

        const table = document.createElement('table');
        table.className = 'data-table';
        const thead = document.createElement('thead');
        const headerRow = document.createElement('tr');
        headerRow.innerHTML = `<th>Gene</th>${columns.map(col => `<th>${col}</th>`).join('')}`;
        thead.appendChild(headerRow);
        table.appendChild(thead);

        const tbody = document.createElement('tbody');
        allGeneNames.forEach(gene => {
            const d = data.find(x => x.gene === gene);
            const row = document.createElement('tr');
            row.innerHTML = `<td>${gene}</td>${d ? d.values.map(v => `<td>${v}</td>`).join('') : columns.map(() => '<td>N/A</td>').join('')}`;
            tbody.appendChild(row);
        });
        table.appendChild(tbody);
        tableContainer.appendChild(table);
    }


    function createSingleConditionPlotForB(data) {
         const columns = dataCategories[currentTab].columns;
        if (columns.length === 0) return;
        const singleCol = columns[0];

        const geneNames = data.map(d => d.gene);
        const y = geneNames;
        const x = Array(geneNames.length).fill('Virion');
        const markerColor = data.map(d => colorPalettes.localization[d.metadata.localization] || '#7f7f7f');
        const hoverText = data.map(d => {
            const val = d.values[0];
            const abd = parseFloat(val);
            const loc = d.metadata.localization;
            return `Gene: ${d.gene}<br>${singleCol}: ${abd}<br>Loc: ${loc}`;
        });

        const plotData = [{
            x: x,
            y: y,
            mode: 'markers',
            type: 'scatter',
            hoverinfo: 'text',
            text: hoverText,
            marker: {
                size: 10,
                color: markerColor,
                line: { width: 1, color: '#333' },
                opacity: 0.7
            },
            hovertemplate: '%{text}<extra></extra>'
        }];

        const layout = {
            title: dataCategories[currentTab].title,
            xaxis: { title: 'Virion', automargin: true, showticklabels: false },
            yaxis: { title: 'Genes', automargin: true, type: 'category', categoryorder: 'array', categoryarray: geneNames },
            margin: { t: 50, r: 50, b: 100, l: 200 },
            height: 800,
            hovermode: 'closest'
        };

        Plotly.newPlot('mainVisualization', plotData, layout, { responsive: true });
    }

    function createLegend(categories, colors) {
        const legendContainer = document.getElementById('legendContainer');
        if (!legendContainer) return;
        legendContainer.innerHTML = '';
        categories.forEach((cat, i) => {
            const item = document.createElement('div');
            item.style.display = 'flex';
            item.style.alignItems = 'center';

            const colorBox = document.createElement('div');
            colorBox.style.width = '15px';
            colorBox.style.height = '15px';
            colorBox.style.marginRight = '5px';
            colorBox.style.backgroundColor = colors[i];
            colorBox.style.border = '1px solid #ccc';

            const label = document.createElement('span');
            label.textContent = cat;

            item.appendChild(colorBox);
            item.appendChild(label);
            legendContainer.appendChild(item);
        });
    }


    function updateVisualization() {
        const data = filterDataForDisplay();
        const columns = dataCategories[currentTab].columns;
        const descEl = document.getElementById('dataDescription');
        if (descEl) descEl.textContent = dataCategories[currentTab].description;

        const vizContainer = document.getElementById('mainVisualization');
        if (vizContainer) vizContainer.innerHTML = '';
        const legendContainer = document.getElementById('legendContainer');
        if (legendContainer) legendContainer.innerHTML = '';

        const dataType = dataCategories[currentTab].dataType;

         if (currentTab === 'B') {
            if (currentView === 'heatmap') {
                createSingleConditionPlotForB(data);
            } else if (currentView === 'lineplot') {
                 createSingleConditionPlotForB(data);
            } else if (currentView === 'table') {
                createDataTable(data, columns);
            }
            return;
        }

        if (currentView === 'heatmap') {
            if (dataType === 'numeric') {
                createHeatmap(data, columns);
            } else if (dataType === 'categorical') {
                createCategoricalHeatmap(data, columns, 'localization');
            } else if (dataType === 'binary') {
                createCategoricalHeatmap(data, columns, 'hcpi');
            } else if (dataType === 'mixed') {
                  if (isAnyNumeric(data)) createHeatmap(data, columns);
                else createDataTable(data, columns);
            }
        } else if (currentView === 'lineplot') {
             if(dataType==='numeric'||dataType==='mixed') {
                if(isAnyNumeric(data)) createLinePlot(data, columns);
                else createDataTable(data, columns);
            } else {
                createDataTable(data, columns);
            }
        } else if (currentView === 'table') {
            createDataTable(data, columns);
        }
    }
    function isAnyNumeric(data) {
      return data.some(d => d.values.some(v => !isNaN(parseFloat(v))));
    }

    function setupEventListeners() {
       const tabButtons = document.querySelectorAll('.tab-button');
        tabButtons.forEach(button => {
            button.addEventListener('click', e => {
                tabButtons.forEach(b => b.classList.remove('active'));
                e.target.classList.add('active');
                currentTab = e.target.dataset.tab;
                 setActiveViewButton('heatmapView');
                currentView = 'heatmap';
                setupFilters();
                updateVisualization();
            });
        });

         const viewButtons = document.querySelectorAll('.view-btn');
        viewButtons.forEach(button => {
            button.addEventListener('click', e => {
                viewButtons.forEach(b => b.classList.remove('active'));
                e.target.classList.add('active');
                currentView = e.target.id.replace('View', '').toLowerCase();
                updateVisualization();
            });
        });


        const searchInput = document.getElementById('geneSearch');
        if (searchInput) {
            searchInput.addEventListener('input', () => updateVisualization());
        }

        const downloadBtn = document.getElementById('downloadData');
        if (downloadBtn) downloadBtn.addEventListener('click', downloadCurrentData);

         const toggleIncompleteBtn = document.getElementById('toggleIncomplete');
        if (toggleIncompleteBtn) {
            toggleIncompleteBtn.addEventListener('click', () => {
                hideIncomplete = !hideIncomplete;
                toggleIncompleteBtn.textContent = hideIncomplete ? "Show All" : "Hide Incomplete";
                updateVisualization();
            });
        }

          const toggleRelativeBtn = document.getElementById('toggleRelative');
        if (toggleRelativeBtn) {
            toggleRelativeBtn.addEventListener('click', () => {
                useRelative = !useRelative;
                toggleRelativeBtn.textContent = useRelative ? "Use Absolute Abundance" : "Use Relative Abundance";
                updateVisualization();
            });
        }

          const mainViz = document.getElementById('mainVisualization');
        mainViz.addEventListener('plotly_click', function (event) {
            if (event && event.points && event.points.length > 0) {
                const gene = event.points[0].y;
                displayGeneDetails(gene);
                displayStatistics(gene);
            }
        });
    }

    function setActiveViewButton(activeButtonId) {
         const viewButtons = document.querySelectorAll('.view-btn');
        viewButtons.forEach(button => {
            if (button.id === activeButtonId) button.classList.add('active');
            else button.classList.remove('active');
        });
    }

    function downloadCurrentData() {
        const data = filterDataForDisplay();
        const columns = dataCategories[currentTab].columns;
        const csv = [
            ['Gene', ...columns].join(','),
            ...allGeneNames.map(gene => {
                const d = data.find(x => x.gene === gene);
                return d ? [gene, ...d.values].join(',') : [gene, ...columns.map(() => 'N/A')].join(',');
            })
        ].join('\n');

        const blob = new Blob([csv], { type: 'text/csv' });
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `hcmv_${currentTab}_data.csv`;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        window.URL.revokeObjectURL(url);
    }

     function setupFilters() {
         const temporalClassSelect = document.getElementById('temporalClassSelect');
        if (temporalClassSelect) {
            temporalClassSelect.innerHTML = '<option value="all">All Temporal Classes</option>';
            const classes = Array.from(new Set(processedData[currentTab].map(d => d.metadata.temporalClass))).sort();
            classes.forEach(cls => {
                const option = document.createElement('option');
                option.value = cls;
                option.textContent = cls;
                temporalClassSelect.appendChild(option);
            });
            temporalClassSelect.removeEventListener('change', updateVisualization);
            temporalClassSelect.addEventListener('change', () => updateVisualization());
        }

         const dataType = dataCategories[currentTab].dataType;
        if (dataType === 'numeric' || dataType === 'mixed') {
            setupAbundanceSlider();
        } else {
             const slider = document.getElementById('abundanceSlider');
            if (slider && slider.noUiSlider) {
                slider.noUiSlider.destroy();
                slider.innerHTML = '';
            }
        }
    }

   function setupAbundanceSlider() {
     const slider = document.getElementById('abundanceSlider');
        if (!slider) return;

        let currentData = processedData[currentTab];
         const nums = currentData.flatMap(d => d.values.map(v => parseFloat(v)).filter(n => !isNaN(n)));
        if (nums.length === 0) {
            if (slider.noUiSlider) { slider.noUiSlider.destroy(); slider.innerHTML = ''; }
            return;
        }
        const minVal = Math.min(...nums);
        const maxVal = Math.max(...nums);

        if (!slider.noUiSlider) {
            noUiSlider.create(slider, {
                start: [minVal, maxVal],
                connect: true,
                range: { 'min': minVal, 'max': maxVal },
                tooltips: true,
                format: {
                    to: value => value.toFixed(2),
                    from: value => Number(value)
                }
            });
             slider.noUiSlider.on('update', () => updateVisualization());
        } else {
            slider.noUiSlider.updateOptions({
                range: { min: minVal, max: maxVal },
                start: [minVal, maxVal]
            });
        }
    }


    function displayGeneDetails(gene) {
        const detailsEl = document.getElementById('geneDetails').querySelector('.details-content');
        if (!detailsEl) return;
        const catData = Object.values(rawData).flat();
        const geneData = catData.find(d => d.Gene === gene);
        if (geneData) {
            detailsEl.innerHTML = `
                <strong>Gene:</strong> ${geneData.Gene}<br>
                <strong>Temporal_Class:</strong> ${geneData['Temporal_Class'] || 'N/A'}<br>
                <strong>Localization:</strong> ${geneData['Loc.'] || 'N/A'}<br>
                <strong>Abundance:</strong> ${geneData['Abd.'] || 'N/A'}<br>
                <strong>HCIP:</strong> ${geneData['HCIP'] || 'N/A'}<br>
                <strong>P1:</strong> ${geneData['P1'] || 'N/A'}<br>
                <strong>P2:</strong> ${geneData['P2'] || 'N/A'}
            `;
        } else {
            detailsEl.textContent = 'Gene details not found.';
        }
    }
  function displayStatistics(gene) {
        const statsEl = document.getElementById('statsContent');
        if (!statsEl) return;
        const geneRow = rawData[currentTab].find(d => d.Gene === gene);
        if (geneRow && dataCategories[currentTab].columns.length > 0) {
             const cols = dataCategories[currentTab].columns;
            const nums = cols.map(c => parseFloat(geneRow[c])).filter(n => !isNaN(n));
            const meanAbundance = nums.length > 0 ? (nums.reduce((a, b) => a + b, 0) / nums.length).toFixed(2) : 'N/A';
            statsEl.innerHTML = `
                <strong>Mean Abundance (Current Tab):</strong> ${meanAbundance}<br>
                 <strong>Temporal_Class:</strong> ${geneRow['Temporal_Class']||'N/A'}<br>
                 <strong>HCIP:</strong> ${geneRow['HCIP']||'N/A'}<br>
                <strong>P1:</strong> ${geneRow['P1']||'N/A'}<br>
                <strong>P2:</strong> ${geneRow['P2']||'N/A'}
            `;
        } else {
            statsEl.textContent = 'Statistics not available for this gene.';
        }
    }
    function showLoading(show) {
        const loadingIndicator = document.getElementById('loadingIndicator');
        if(loadingIndicator) {
           loadingIndicator.classList.toggle('show',show);
        }
     }
    function handleError(error) {
      console.error("Error:", error);
        const errorDiv = document.getElementById('errorMessage');
        if (errorDiv) {
            errorDiv.textContent = 'An error occurred: ' + error;
            errorDiv.style.display = 'block';
        }
    }
</script>
