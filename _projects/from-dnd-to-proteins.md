---
layout: default
excerpt: A dive into protein predictions and conformational changes in the cellular transport protein Rab3a.
title: From Dungeons and Dragons to Proteins and Predictions
category: ai
presented_at: WSUSOM Biochemistry, Molecular Biology, and Immunology Departmental Retreat 2023
---

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>From Dungeons and Dragons to Proteins and Predictions</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <style>
        body {
            font-family: 'Merriweather', serif;
            line-height: 1.6;
            color: #333;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f0e6d2;
        }
        h1, h2, h3 {
            font-family: 'Dragon Hunter', fantasy;
            color: #8b0000;
        }
        .hero {
            background-image: url('https://via.placeholder.com/1200x400');
            background-size: cover;
            color: white;
            text-align: center;
            padding: 100px 20px;
            margin-bottom: 40px;
        }
        .hero h1 {
            font-size: 3em;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        }
        .section {
            background-color: #fff;
            border-radius: 10px;
            padding: 30px;
            margin-bottom: 40px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .flex-container {
            display: flex;
            justify-content: space-between;
            flex-wrap: wrap;
        }
        .flex-item {
            flex-basis: 48%;
            margin-bottom: 20px;
        }
        img {
            max-width: 100%;
            height: auto;
            border-radius: 10px;
        }
        .video-container {
            max-width: 100%;
            margin: 20px 0;
        }
        .video-container video {
            width: 100%;
            height: auto;
            display: block;
        }
        .quote {
            font-style: italic;
            border-left: 4px solid #8b0000;
            padding-left: 20px;
            margin: 20px 0;
        }
        .interactive-element {
            background-color: #f0f0f0;
            border-radius: 10px;
            padding: 20px;
            margin-top: 20px;
        }
        .protein-viewer {
            width: 100%;
            height: 400px;
        }
        @font-face {
            font-family: 'Dragon Hunter';
            src: url('path-to-your-custom-font.woff2') format('woff2');
        }
        .dice {
            font-size: 2em;
            cursor: pointer;
        }
        .spell-book {
            background-color: #f9e4b7;
            border: 2px solid #8b4513;
            border-radius: 10px;
            padding: 20px;
            margin-top: 20px;
        }
        .spell {
            margin-bottom: 10px;
        }
        .spell-name {
            font-weight: bold;
            color: #8b0000;
        }
        .reference {
            color: #8b0000;
            cursor: pointer;
            text-decoration: none;
        }

        .reference:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="hero">
        <h1>From Dungeons and Dragons to Proteins and Predictions</h1>
        <p>An Adventure Into the Realm of Molecular Biology</p>
    </div>

    <div class="section">
        <h2>The Double Helix Tavern: Where Fantasy Meets Science</h2>
        <p>Welcome, brave adventurers and curious scientists, to the grand tavern where our journey begins. Just as diverse parties gather in D&D to embark on fantastical journeys, we find ourselves at the crossroads of imagination and scientific discovery. Our mission? To travel through the complex landscape of protein folding, wielding the powerful magic of machine learning and the ancient wisdom of biochemistry.</p>
        <div class="flex-container">
            <div class="flex-item">
                <img src="https://via.placeholder.com/500x300" alt="D&D tavern scene">
                <p>The Double Helix Tavern: Where adventurers and scientists alike gather to plan their quests</p>
            </div>
            <div class="flex-item">
                <img src="https://via.placeholder.com/500x300" alt="Scientific laboratory">
                <p>The Alchemist's Lab: Where the magic of science unfolds</p>
            </div>
        </div>
        <p>In the Double Helix Tavern, barbarians and biochemists, wizards and bioinformaticians sit side by side, sharing tales of conquered dungeons and deciphered protein structures. For in our world, the challenges of understanding molecular biology is  no less difficult than facing a fearsome dragon.</p>
    </div>

    <div class="section">
        <h2>Character Creation: The Art of Protein Design</h2>
        <p>In D&D, we craft unique characters with distinct abilities and backstories. Similarly, in the realm of protein science, we encounter fascinating molecular 'characters' with their own special traits and functions. Let's meet two of our protein protagonists: Pip and Toby, the duck-loving adventurers.</p>
        <div class="flex-container">
            <div class="flex-item">
                <img src="https://via.placeholder.com/500x300" alt="Pip, the duck loving adventurer">
                <p>Pip, the duck-loving adventurer (Rab3A in its GTP-bound state)</p>
            </div>
            <div class="flex-item">
                <img src="https://via.placeholder.com/500x300" alt="Toby, Pip's duck loving twin brother">
                <p>Toby, Pip's duck-loving twin brother (Rab3A in its GDP-bound state)</p>
            </div>
        </div>
        <p>Just as a skilled Dungeon Master brings characters to life through vivid descriptions and role-playing, we use advanced AI models like AlphaFold to visualize and predict protein structures. But our 'characters' - the proteins - are far more complex than any D&D character sheet could capture.</p>
        <div class="interactive-element">
            <h3>Roll for Protein Stats</h3>
            <p>Click the dice to generate random protein characteristics:</p>
            <div class="dice" onclick="rollProteinStats()">🎲</div>
            <div id="protein-stats"></div>
        </div>
    </div>

    <div class="section">
        <h2>Casting Spells: The Arcane Art of Diffusion Models</h2>
        <p>In the mystical world of D&D, spellcasters shape reality with incantations and gestures. In the scientific realm, we wield equally powerful magic in the form of diffusion models - a type of machine learning algorithm that can generate images from text descriptions, much like a wizard conjuring visions from thin air.</p>
        <div class="flex-container">
            <div class="flex-item">
                <img src="https://via.placeholder.com/500x300" alt="Diffusion model process">
                <p>The arcane process of diffusion models: From noise to clear images</p>
            </div>
            <div class="flex-item">
                <p class="quote">"a half elf man holding two ducks"</p>
                <p>Our incantation (prompt) for the diffusion model</p>
            </div>
        </div>
        <p>But how do these magical diffusion models work? Imagine a reverse entropy spell, where order emerges from chaos. The model starts with random noise and gradually refines it, guided by our textual incantation, until a clear image emerges. This process mirrors the protein folding problem, where an ordered 3D structure emerges from an apparently random string of amino acids.</p>
        <div class="spell-book">
            <h3>Spellbook of Protein Prediction</h3>
            <div class="spell">
                <span class="spell-name">Summon Protein Structure:</span> Use AlphaFold to predict a protein's 3D structure from its amino acid sequence.
            </div>
            <div class="spell">
                <span class="spell-name">Conjure Molecular Dynamics:</span> Simulate the motion and flexibility of proteins over time.
            </div>
            <div class="spell">
                <span class="spell-name">Scry Binding Sites:</span> Identify potential ligand binding sites on a protein's surface.
            </div>
        </div>
    </div>

    <div class="section">
        <h2>Rolling the Dice: The Probabilistic Nature of Protein Folding</h2>
        <p>In D&D, the roll of a dice determines the outcome of actions. In the world of protein folding, we face a similar element of chance and probability. The folding of a protein is not a deterministic process, but rather a stochastic one, influenced by thermodynamics and kinetics.</p>
        <h3>The Rab3A Quest: Unraveling the Mystery of Dynamic Switch Regions</h3>
        <p>Our party's current quest focuses on understanding the dynamic switch regions of Rab proteins, particularly Rab3A. These regions are as changeable as a shapeshifter, altering their conformation based on whether they're bound to GTP or GDP.</p>
        <ul>
            <li>Switch I: The Rogue of our protein party, quick and elusive, it changes conformation rapidly.</li>
            <li>Interswitch: The Bard, bridging different parts of the protein and facilitating communication between domains.</li>
            <li>Switch II: The Barbarian, capable of dramatic conformational changes that can significantly alter the protein's function.</li>
        </ul>
        <img src="https://via.placeholder.com/800x400" alt="Rab protein switch regions">
        <p>The three switch regions of Rab proteins, each playing a crucial role in the protein's function and interactions</p>
        <p>Understanding these switch regions is crucial because they determine how Rab3A interacts with other proteins and membranes, controlling vital cellular processes like vesicle trafficking. It's akin to understanding the key pressure points or weak spots of a formidable boss in a D&D campaign.</p>
    </div>

    <div class="section">
        <h2>Consulting the Oracle: The Prophecies of AlphaFold</h2>
        <p>In our scientific campaign, AlphaFold serves as our oracle, providing predictions about protein structures with unprecedented accuracy. Like the cryptic utterances of a D&D oracle, AlphaFold's predictions require careful interpretation<span class="reference" data-ref="ref1" onclick="scrollToReference('ref1', event)">[1]</span>. Let's examine its predictions for Rab3A:</p>
        <div id="plddt-plot"></div>
        <p>This graph shows the predicted Local Distance Difference Test (pLDDT) scores for Rab3A. In the language of our quest:</p>
        <ul>
            <li>High pLDDT scores (above 90) are like rolling a natural 20 - these regions are predicted with high confidence and are likely to be well-ordered in the protein structure.</li>
            <li>Moderate scores (between 70 and 90) are like rolling 10-19 - these regions are predicted with some confidence but may have some flexibility.</li>
            <li>Low scores (below 50) are like rolling a natural 1 - these regions are likely to be disordered or highly flexible, defying precise structural prediction.</li>
        </ul>
        <p>Notice how the switch regions (Switch 1, Interswitch, and Switch 2) show varying levels of confidence. This reflects their dynamic nature, hinting at their role in the protein's function.</p>
        <div class="interactive-element">
            <h3>Protein Structure Viewer</h3>
            <p>Interact with the 3D structure of Rab3A:</p>
            <div id="protein-viewer" class="protein-viewer"></div>
        </div>
    </div>

    <div class="section">
        <h2>Mapping the Dungeon: The Magic of t-SNE Visualization</h2>
        <p>To visualize the complex multidimensional data of our protein structures, we employ a powerful scrying technique known as t-distributed stochastic neighbor embedding (t-SNE). This is akin to a magical map that reveals hidden patterns and relationships in our molecular dungeon.</p>
        <div id="tsne-plot"></div>
        <p>In this t-SNE plot, each point represents a different prediction or conformation of Rab3A. Clusters of points suggest similar conformations, while isolated points might represent unique or rare states of the protein. This map helps us understand the 'landscape' of possible Rab3A structures, much like a well-drawn dungeon map reveals the layout of chambers and corridors.</p>
        <p>The colors in the plot represent different features or conditions, such as:</p>
        <ul>
            <li>Red: GTP-bound state (active form)</li>
            <li>Blue: GDP-bound state (inactive form)</li>
            <li>Green: Conformations with high flexibility in switch regions</li>
            <li>Yellow: Conformations with bound effector proteins</li>
        </ul>
        <p>By studying this map, we can identify patterns and relationships that might not be apparent from looking at individual structures, helping us to understand the full range of Rab3A's potential behaviors and interactions.</p>
    </div>

<div class="section">
        <h2>Right Tool for the Job: Full MSA vs Subsampled MSA</h2>
        <p>Tools are the lifeblood of adventurers.  :</p>
        <ul>
            <li><strong>Computational Resources:</strong> Full MSA is like casting a high-level spell that requires a lot of mana (computational power). Subsampled MSA is a lower-level spell that can be cast more quickly and frequently.</li>
            <li><strong>Time Constraints:</strong> In a fast-paced battle (or research project with tight deadlines), the quicker Subsampled MSA might be preferable.</li>
            <li><strong>Protein Complexity:</strong> For a complex boss battle (highly divergent or structurally complex proteins), the Full MSA might be necessary to capture all the nuances.</li>
            <li><strong>Sequence Diversity:</strong> If your protein family is like a diverse party of adventurers, Subsampled MSA might provide a good representation without redundancy.</li>
        </ul>
        <div class="interactive-element">
            <h3>MSA Strategy Simulator</h3>
            <p>Choose your MSA strategy and see how it affects your protein prediction quest:</p>
            <select id="msa-strategy">
                <option value="full">Full MSA (Legendary Sword)</option>
                <option value="subsampled">Subsampled MSA (Mythical Bow)</option>
            </select>
            <button onclick="simulateMSAStrategy()">Embark on Quest</button>
            <div id="msa-result"></div>
        </div>
    </div>

    <div class="section">
        <h2>The Animated Spell: Bringing Protein Motion to Life</h2>
        <p>Just as a skilled illusionist might bring a scene to life with magic, we use molecular dynamics simulations and animations to visualize the dynamic nature of protein structures. Behold, the mesmerizing dance of Rab3A's switch region!</p>
        <div class="video-container">
            <video id="protein-motion-video" controls loop>
                <source src="/assets/videos/Rab3A_GTP_Movie_wideview_one to 26.mp4" type="video/mp4">
                Your browser does not support the video tag.
            </video>
        </div>
        <p>This animation showcases the flexibility and movement of the switch region, a critical aspect of Rab3A's function that static models cannot fully capture. It's like watching a shape-shifting monster in D&D - the protein's form changes in response to its environment and binding partners.</p>
        <p>Key observations from this molecular choreography:</p>
        <ul>
            <li>The Switch I region (in red) shows high flexibility, oscillating between open and closed conformations.</li>
            <li>The Interswitch region (in yellow) acts as a hinge, facilitating the movement of Switch I and II.</li>
            <li>Switch II (in blue) undergoes a dramatic conformational change upon GTP hydrolysis, like a trap springing in a dungeon.</li>
        </ul>
    </div>

    <div class="section">
        <h2>Advanced Class: Machine Learning in Protein Science</h2>
        <p>As our adventurers gain experience, they can choose to specialize in advanced classes. In the realm of protein science, one such advanced class is the application of machine learning. Let's explore some of these powerful techniques:</p>
        
        <h3>1. Convolutional Neural Networks (CNNs) for Protein-Ligand Binding Prediction</h3>
        <p>CNNs, originally designed for image recognition, can be adapted to predict protein-ligand binding sites. It's like training a ranger to spot hidden creatures, but instead, we're spotting potential binding pockets on a protein's surface.</p>
        <div class="spell-book">
            <div class="spell">
                <span class="spell-name">Voxelize Protein Structure:</span> Convert 3D protein structure into a grid of voxels, each containing information about the local chemical environment.
            </div>
            <div class="spell">
                <span class="spell-name">Apply 3D Convolutions:</span> Use 3D convolutional filters to detect patterns in the voxelized structure, identifying potential binding sites.
            </div>
        </div>

        <h3>2. Recurrent Neural Networks (RNNs) for Protein Sequence Analysis</h3>
        <p>RNNs excel at processing sequential data, making them ideal for analyzing protein sequences. This is akin to a bard reciting an epic tale, where each word (or amino acid) is understood in the context of what came before.</p>
        <div class="spell-book">
            <div class="spell">
                <span class="spell-name">Encode Amino Acids:</span> Represent each amino acid as a vector, capturing its chemical properties.
            </div>
            <div class="spell">
                <span class="spell-name">LSTM Magic:</span> Use Long Short-Term Memory (LSTM) cells to capture long-range dependencies in the sequence, predicting structural or functional properties.
            </div>
        </div>

        <h3>3. Graph Neural Networks (GNNs) for Modeling Protein Structure</h3>
        <p>Proteins can be represented as graphs, with amino acids as nodes and interactions as edges. GNNs can process these graphs to predict properties or generate new structures. It's like a druid understanding the interconnectedness of a forest ecosystem, but applied to the molecular world.</p>
        <div class="spell-book">
            <div class="spell">
                <span class="spell-name">Construct Protein Graph:</span> Represent amino acids as nodes and their interactions (hydrogen bonds, hydrophobic interactions) as edges.
            </div>
            <div class="spell">
                <span class="spell-name">Message Passing:</span> Allow information to flow through the graph, updating node and edge features to capture the global structure.
            </div>
        </div>
    </div>

    <div class="section">
        <h2>The Philosopher's Stone: Generative Models for Protein Design</h2>
        <p>The ultimate quest in protein science is not just to understand existing proteins, but to design new ones with desired properties. This is like crafting legendary artifacts in D&D, but at the molecular level. Enter the realm of generative models:</p>

        <h3>1. Variational Autoencoders (VAEs) for Protein Generation</h3>
        <p>VAEs learn a compressed representation of protein sequences or structures, allowing us to generate new proteins by sampling from this latent space. It's like distilling the essence of many proteins into a magical elixir, from which new proteins can be conjured.</p>

        <h3>2. Generative Adversarial Networks (GANs) for Protein Design</h3>
        <p>GANs pit two neural networks against each other: a generator creating new proteins, and a discriminator trying to distinguish real proteins from generated ones. This adversarial training results in increasingly realistic protein designs, much like two rival wizards trying to outdo each other in creating the most convincing illusions.</p>

        <div class="interactive-element">
            <h3>Protein Generator</h3>
            <p>Generate a new protein sequence using our AI model:</p>
            <button onclick="generateProtein()">Create New Protein</button>
            <div id="generated-protein"></div>
        </div>
    </div>

    <div class="section">
        <h2>The Final Boss: Challenges in Protein Prediction and Design</h2>
        <p>As with any epic quest, we face formidable challenges in our journey through protein science:</p>
        <ul>
            <li><strong>The Protein Folding Problem:</strong> Despite advances like AlphaFold, accurately predicting the structure of all proteins remains a grand challenge, especially for disordered regions and membrane proteins.</li>
            <li><strong>Designing Functional Proteins:</strong> Creating proteins with specific functions is like trying to craft a magic item with exact properties - it requires deep understanding and often involves trial and error.</li>
            <li><strong>Modeling Protein Dynamics:</strong> Proteins are not static structures but constantly moving entities. Capturing this motion computationally is a ongoing challenge.</li>
            <li><strong>Protein-Protein Interactions:</strong> Predicting how proteins interact with each other is crucial for understanding cellular processes but remains difficult due to the complexity of these interactions.</li>
        </ul>
    </div>

    <div class="section">
        <h2>Epilogue: The Never-Ending Quest</h2>
        <p>Our journey through the realm of protein prediction and design is an ongoing adventure. Each discovery opens up new questions, each answered riddle reveals new mysteries. As we continue to develop more powerful computational "spells" and gather more experimental "lore", we edge closer to unraveling the deepest secrets of the protein universe.</p>
        <p>Remember, brave scientist-adventurers: in the game of protein science, as in Dungeons and Dragons, creativity, perseverance, and teamwork are your most powerful allies. May your pipettes be ever accurate and your computations swift!</p>
        <div class="quote">
            "In the vast dungeon of the cellular world, proteins are both the treasure we seek and the monsters we face. Our quest to understand them is the grandest adventure in modern biology." - The Archmage of Protein Dynamics
        </div>
    </div>

    <div class="section" id="references">
        <h2>Spellbook of Knowledge: References</h2>
        <ol id="reference-list">
            <li id="ref1">Jumper, J., Evans, R., Pritzel, A. et al. Highly accurate protein structure prediction with AlphaFold. Nature 596, 583–589 (2021).</li>
            <li id="ref2">Baek, M., DiMaio, F., Anishchenko, I. et al. Accurate prediction of protein structures and interactions using a three-track neural network. Science 373, 871–876 (2021).</li>
            <li id="ref3">Senior, A.W., Evans, R., Jumper, J. et al. Improved protein structure prediction using potentials from deep learning. Nature 577, 706–710 (2020).</li>
            <li id="ref4">Elnaggar, A., Heinzinger, M., Dallago, C. et al. ProtTrans: towards cracking the language of Life's code through self-supervised deep learning and high performance computing. IEEE Trans Pattern Anal Mach Intell. (2021).</li>
            <li id="ref5">Yang, J., Anishchenko, I., Park, H. et al. Improved protein structure prediction using predicted interresidue orientations. Proc Natl Acad Sci USA 117, 1496–1503 (2020).</li>
        </ol>
    </div>

    <script>
        // Protein stats generator
        function rollProteinStats() {
            const stats = {
                'Molecular Weight': Math.floor(Math.random() * 100000) + 10000,
                'Isoelectric Point': (Math.random() * 14).toFixed(2),
                'Alpha Helix %': Math.floor(Math.random() * 100),
                'Beta Sheet %': Math.floor(Math.random() * 100),
                'Binding Affinity': (Math.random() * 10).toFixed(2) + ' nM'
            };
            let statsHtml = '<ul>';
            for (let [key, value] of Object.entries(stats)) {
                statsHtml += `<li>${key}: ${value}</li>`;
            }
            statsHtml += '</ul>';
            document.getElementById('protein-stats').innerHTML = statsHtml;
        }

        // MSA strategy simulator
        function simulateMSAStrategy() {
            const strategy = document.getElementById('msa-strategy').value;
            let result = '';
            if (strategy === 'full') {
                result = 'You chose the Legendary Sword (Full MSA). Your prediction is highly accurate but took 3 days to complete. You gained deep insights into the protein's evolutionary history.';
            } else {
                result = 'You chose the Mythical Bow (Subsampled MSA). Your prediction completed in 3 hours with good accuracy. You identified key functional regions quickly.';
            }
            document.getElementById('msa-result').innerText = result;
        }

        function scrollToReference(refId, event) {
            event.preventDefault(); // Prevent default link behavior
            const refElement = document.getElementById(refId);
            if (refElement) {
                const yOffset = -100; // Adjust this value to fine-tune the scroll position
                const y = refElement.getBoundingClientRect().top + window.pageYOffset + yOffset;
                window.scrollTo({top: y, behavior: 'smooth'});
                
                // Highlight the reference briefly
                refElement.style.backgroundColor = '#ffff99';
                setTimeout(() => {
                    refElement.style.backgroundColor = 'transparent';
                }, 2000);
            }
        }

        // Protein generator
        function generateProtein() {
            const aminoAcids = 'ACDEFGHIKLMNPQRSTVWY';
            let sequence = '';
            for (let i = 0; i < 100; i++) {
                sequence += aminoAcids[Math.floor(Math.random() * aminoAcids.length)];
            }
            document.getElementById('generated-protein').innerText = 'Generated Protein Sequence: ' + sequence;
        }

        // Plotly for pLDDT plot
        Plotly.newPlot('plddt-plot', [{
            x: Array.from({length: 220}, (_, i) => i + 1),
            y: Array.from({length: 220}, () => Math.random() * 100),
            type: 'scatter'
        }], {
            title: 'pLDDT Scores for Rab3A',
            xaxis: {title: 'Residue Position'},
            yaxis: {title: 'pLDDT Score'}
        });

        // Plotly for t-SNE plot
        Plotly.newPlot('tsne-plot', [{
            x: Array.from({length: 100}, () => Math.random() * 10 - 5),
            y: Array.from({length: 100}, () => Math.random() * 10 - 5),
            mode: 'markers',
            type: 'scatter',
            marker: {color: Array.from({length: 100}, () => Math.floor(Math.random() * 4))}
        }], {
            title: 't-SNE Visualization of Rab3A Conformations',
            xaxis: {title: 't-SNE 1'},
            yaxis: {title: 't-SNE 2'}
        });

        // Three.js for protein viewer

        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(75, 1, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer();
        renderer.setSize(400, 400);
        document.getElementById('protein-viewer').appendChild(renderer.domElement);

        const geometry = new THREE.SphereGeometry(1, 32, 32);
        const material = new THREE.MeshBasicMaterial({color: 0x00ff00});
        const sphere = new THREE.Mesh(geometry, material);
        scene.add(sphere);

        camera.position.z = 5;

        function animate() {
            requestAnimationFrame(animate);
            sphere.rotation.x += 0.01;
            sphere.rotation.y += 0.01;
            renderer.render(scene, camera);
        }
        animate();
    </script>
</body>
</html>

