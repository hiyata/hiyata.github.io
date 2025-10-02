// virus-classifier.js

document.addEventListener('DOMContentLoaded', function() {
    const fileInput = document.getElementById('fastaFile');
    const analyzeButton = document.getElementById('analyzeButton');
    const resultsSection = document.getElementById('results');
    const loadingSection = document.getElementById('loading');
    const predictionOutput = document.getElementById('predictionOutput');

    // Load Gradio client script dynamically
    const script = document.createElement('script');
    script.src = 'https://cdn.jsdelivr.net/npm/@gradio/client@2.3.0/dist/gradio.umd.min.js';
    document.head.appendChild(script);

    // Function to parse FASTA header
    function parseFastaHeader(file) {
        return new Promise((resolve) => {
            const reader = new FileReader();
            reader.onload = (e) => {
                const content = e.target.result;
                const lines = content.split('\n');
                const headers = lines
                    .filter(line => line.startsWith('>'))
                    .map(line => line.substring(1).trim());
                resolve(headers);
            };
            reader.readAsText(file);
        });
    }

    // Add status message to UI
    function updateStatus(message, isError = false) {
        const statusDiv = document.createElement('div');
        statusDiv.className = isError ? 'error' : 'status';
        statusDiv.textContent = message;
        predictionOutput.appendChild(statusDiv);
        console.log(message);
    }

    // Enable/disable analyze button and show FASTA header
    fileInput.addEventListener('change', async function() {
        const file = this.files[0];
        analyzeButton.disabled = !file;
        
        if (file) {
            const headers = await parseFastaHeader(file);
            predictionOutput.innerHTML = `
                <div class="file-info">
                    <h4>Selected sequences:</h4>
                    ${headers.map(header => `<p>${header}</p>`).join('')}
                </div>
            `;
            resultsSection.style.display = 'block';
        } else {
            resultsSection.style.display = 'none';
        }
    });

    // Handle file analysis
    analyzeButton.addEventListener('click', async function() {
        const file = fileInput.files[0];
        if (!file) return;

        try {
            // Show loading state
            loadingSection.style.display = 'block';
            analyzeButton.disabled = true;
            predictionOutput.innerHTML = ''; // Clear previous results

            updateStatus('Loading Gradio client...');

            // Wait for Gradio client to load if necessary
            if (!window.gradio) {
                await new Promise((resolve, reject) => {
                    script.onload = resolve;
                    script.onerror = () => reject(new Error('Failed to load Gradio client'));
                });
            }

            updateStatus('Initializing connection to Hugging Face Space...');
            
            // Initialize Gradio client with timeout
            const client = await Promise.race([
                window.gradio.client("hiyata/HostClassifier"),
                new Promise((_, reject) => setTimeout(() => reject(new Error('Connection timeout')), 30000))
            ]);

            updateStatus('Connected. Sending sequence for analysis...');
            
            // Make prediction using the client
            const result = await client.predict("/predict", [
                file // The API expects an array of inputs
            ]);

            updateStatus('Received response from server.');

            // Display results
            const resultData = result.data ? result.data[0] : 'No results returned';
            predictionOutput.innerHTML += `
                <div class="prediction-results">
                    <h4>Analysis Results:</h4>
                    <pre>${resultData}</pre>
                </div>`;
            resultsSection.style.display = 'block';

        } catch (error) {
            console.error('Error:', error);
            updateStatus(`Error: ${error.message}\n\nPlease make sure your file is in valid FASTA format and try again.\n\nTechnical details: ${error.toString()}`, true);
        } finally {
            // Hide loading state
            loadingSection.style.display = 'none';
            analyzeButton.disabled = false;
        }
    });
});