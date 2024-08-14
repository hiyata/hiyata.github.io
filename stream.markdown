---
layout: default
title: ANYA Simulation Live Stream
---

<div class="page-transition-overlay">
    <div class="page-transition-content">
        <h2>Loading ANYA Simulation...</h2>
        <div class="loading-spinner"></div>
    </div>
</div>

<div class="container">
    <h1 class="title">ANYA Simulation Live Stream</h1>
    
    <div class="stream-container">
        <div class="video-wrapper">
            <iframe width="100%" height="100%" src="https://www.youtube.com/embed/live_stream?channel=YOUR_CHANNEL_ID" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        </div>
    </div>

    <div class="info-section">
        <h2>About ANYA Simulation</h2>
        <p>Watch the ANYA simulation unfold in real-time. This project explores the intricate dynamics of viral evolution and adaptation within complex host environments.</p>
    </div>

    <div class="data-visualization">
        <h2>Live Data Visualization</h2>
        <div class="chart-container">
            <canvas id="evolutionChart"></canvas>
        </div>
    </div>

    <div class="interactive-model">
        <h2>Interactive 3D Virus Model</h2>
        <div id="3d-model"></div>
    </div>
</div>

<link rel="stylesheet" href="{{ '/assets/css/stream-transition.css' | relative_url }}">
<script src="{{ '/assets/js/stream-transition.js' | relative_url }}"></script>

<script src="https://cdnjs.cloudflare.com/ajax/libs/animejs/3.2.1/anime.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.7.0/chart.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>

<script>
// Three.js 3D model
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, 1, 0.1, 1000);
const renderer = new THREE.WebGLRenderer();
renderer.setSize(400, 400);
document.getElementById('3d-model').appendChild(renderer.domElement);

const geometry = new THREE.SphereGeometry(1, 32, 32);
const material = new THREE.MeshPhongMaterial({color: 0x00ff9d});
const sphere = new THREE.Mesh(geometry, material);
scene.add(sphere);

const light = new THREE.PointLight(0xffffff, 1, 100);
light.position.set(10, 10, 10);
scene.add(light);

camera.position.z = 5;

function animate() {
  requestAnimationFrame(animate);
  sphere.rotation.x += 0.01;
  sphere.rotation.y += 0.01;
  renderer.render(scene, camera);
}
animate();

// Simulated live data update
setInterval(() => {
  const newData1 = Math.floor(Math.random() * 20);
  const newData2 = Math.floor(Math.random() * 20);
  evolutionChart.data.labels.push('Day ' + (evolutionChart.data.labels.length + 1));
  evolutionChart.data.datasets[0].data.push(newData1);
  evolutionChart.data.datasets[1].data.push(newData2);
  evolutionChart.data.labels.shift();
  evolutionChart.data.datasets[0].data.shift();
  evolutionChart.data.datasets[1].data.shift();
  evolutionChart.update();
}, 5000);
</script>