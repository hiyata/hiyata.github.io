---
layout: default
title: ANYA Simulation Live Stream
---

<div class="container">
  <h1 class="title">ANYA Simulation Live Stream</h1>
  
  <div class="stream-container">
    <div class="video-wrapper">
      <iframe width="100%" height="100%" src="https://www.youtube.com/embed/live_stream?channel=YOUR_CHANNEL_ID" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>
  </div>

  <div class="info-section">
    <h2>About ANYA Simulation</h2>
    <p>Watch the ANYA (Artificial Network for Yielding Adaptations) simulation unfold in real-time. This groundbreaking project explores the intricate dynamics of viral evolution and adaptation within complex host environments.</p>
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

<style>
body {
  font-family: 'Roboto', sans-serif;
  background: linear-gradient(135deg, #1a1a2e, #16213e);
  color: #e0e0e0;
  line-height: 1.6;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.title {
  font-size: 3rem;
  text-align: center;
  margin-bottom: 2rem;
  color: #00ff9d;
  text-shadow: 0 0 10px rgba(0, 255, 157, 0.5);
}

.stream-container {
  background: rgba(255, 255, 255, 0.1);
  border-radius: 15px;
  overflow: hidden;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
}

.video-wrapper {
  position: relative;
  padding-bottom: 56.25%; /* 16:9 aspect ratio */
  height: 0;
}

.video-wrapper iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.info-section, .data-visualization, .interactive-model {
  background: rgba(255, 255, 255, 0.05);
  border-radius: 10px;
  padding: 1.5rem;
  margin-top: 2rem;
}

h2 {
  color: #00ff9d;
  margin-bottom: 1rem;
}

.chart-container {
  height: 300px;
}

#3d-model {
  height: 400px;
  background: #0a0a23;
  border-radius: 10px;
}

@keyframes pulse {
  0% {
    box-shadow: 0 0 0 0 rgba(0, 255, 157, 0.7);
  }
  70% {
    box-shadow: 0 0 0 10px rgba(0, 255, 157, 0);
  }
  100% {
    box-shadow: 0 0 0 0 rgba(0, 255, 157, 0);
  }
}

.interactive-model {
  animation: pulse 2s infinite;
}
</style>

<script src="https://cdnjs.cloudflare.com/ajax/libs/animejs/3.2.1/anime.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.7.0/chart.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>

<script>
// Anime.js animation
anime({
  targets: '.title',
  translateY: [-50, 0],
  opacity: [0, 1],
  easing: 'easeOutElastic(1, .8)',
  duration: 1500,
  delay: 300
});

anime({
  targets: ['.info-section', '.data-visualization', '.interactive-model'],
  translateY: [50, 0],
  opacity: [0, 1],
  easing: 'easeOutExpo',
  duration: 1500,
  delay: anime.stagger(200, {start: 500})
});

// Chart.js
const ctx = document.getElementById('evolutionChart').getContext('2d');
const evolutionChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7'],
    datasets: [{
      label: 'Viral Population',
      data: [12, 19, 3, 5, 2, 3, 10],
      borderColor: 'rgb(0, 255, 157)',
      tension: 0.4
    }, {
      label: 'Host Immune Response',
      data: [5, 15, 8, 12, 7, 10, 6],
      borderColor: 'rgb(255, 99, 132)',
      tension: 0.4
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    scales: {
      y: {
        beginAtZero: true
      }
    },
    plugins: {
      legend: {
        labels: {
          color: '#e0e0e0'
        }
      }
    }
  }
});

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