const TILE_SIZE = 256;

const BASE_URL = 'https://corsproxy.io/?url=https://vmslide.med.wayne.edu/slides';

const SLIDES = {
    'WS_017': 'Lip',
    'WS_036': 'Tongue',
    'WS_028': 'Tooth',
    'SL008': 'Parotid Gland',
    'MCO0081': 'Submandibular Gland',
    'GWU046': 'Sublingual Gland'
};

class HistologyViewer {
    constructor(canvasId = 'slideCanvas') {
        this.canvas = document.getElementById(canvasId);
        this.ctx = this.canvas.getContext('2d');
        
        // State
        this.currentSlide = 'WS_017';
        this.zoom = 1;
        this.offsetX = 0;
        this.offsetY = 0;
        this.annotations = [];
        this.showAnnotations = true;
        this.showGrid = false;
        
        // Performance
        this.tileCache = new Map();
        this.maxCacheSize = 100;
        this.isLoading = false;
        this.lastRenderTime = 0;
        this.fps = 0;
        
        // Mouse/touch
        this.isDragging = false;
        this.lastMouseX = 0;
        this.lastMouseY = 0;
        this.touchDistance = 0;
        
        this.init();
    }
    
    init() {
        this.setupCanvas();
        this.setupEventListeners();
        this.render();
        
        // Start animation loop
        this.animationFrameId = requestAnimationFrame(() => this.animationLoop());
        
        updateStatus('Ready');
    }
    
    setupCanvas() {
        this.canvas.width = this.canvas.offsetWidth;
        this.canvas.height = this.canvas.offsetHeight;
        
        window.addEventListener('resize', () => {
            this.canvas.width = this.canvas.offsetWidth;
            this.canvas.height = this.canvas.offsetHeight;
            this.render();
        });
    }
    
    setupEventListeners() {
        // Mouse events
        this.canvas.addEventListener('mousedown', (e) => this.onMouseDown(e));
        this.canvas.addEventListener('mousemove', (e) => this.onMouseMove(e));
        this.canvas.addEventListener('mouseup', (e) => this.onMouseUp(e));
        this.canvas.addEventListener('mouseleave', (e) => this.onMouseLeave(e));
        this.canvas.addEventListener('wheel', (e) => this.onWheel(e));
        
        // Touch events
        this.canvas.addEventListener('touchstart', (e) => this.onTouchStart(e));
        this.canvas.addEventListener('touchmove', (e) => this.onTouchMove(e));
        this.canvas.addEventListener('touchend', (e) => this.onTouchEnd(e));
        
        // Keyboard events
        document.addEventListener('keydown', (e) => this.onKeyDown(e));
        
        // Double click to fit
        this.canvas.addEventListener('dblclick', () => this.fitToView());
    }
    
    // ==================== Event Handlers ====================
    
    onMouseDown(e) {
        this.isDragging = true;
        this.lastMouseX = e.clientX;
        this.lastMouseY = e.clientY;
        this.canvas.style.cursor = 'grabbing';
    }
    
    onMouseMove(e) {
        if (this.isDragging) {
            const deltaX = e.clientX - this.lastMouseX;
            const deltaY = e.clientY - this.lastMouseY;
            
            this.offsetX -= deltaX;
            this.offsetY -= deltaY;
            
            this.lastMouseX = e.clientX;
            this.lastMouseY = e.clientY;
            
            this.render();
        }
    }
    
    onMouseUp(e) {
        this.isDragging = false;
        this.canvas.style.cursor = 'grab';
    }
    
    onMouseLeave(e) {
        this.isDragging = false;
        this.canvas.style.cursor = 'grab';
    }
    
    onWheel(e) {
        e.preventDefault();
        
        if (e.deltaY < 0) {
            this.zoomIn();
        } else {
            this.zoomOut();
        }
    }
    
    onTouchStart(e) {
        if (e.touches.length === 2) {
            const dx = e.touches[0].clientX - e.touches[1].clientX;
            const dy = e.touches[0].clientY - e.touches[1].clientY;
            this.touchDistance = Math.sqrt(dx * dx + dy * dy);
        } else if (e.touches.length === 1) {
            this.isDragging = true;
            this.lastMouseX = e.touches[0].clientX;
            this.lastMouseY = e.touches[0].clientY;
        }
    }
    
    onTouchMove(e) {
        if (e.touches.length === 2) {
            const dx = e.touches[0].clientX - e.touches[1].clientX;
            const dy = e.touches[0].clientY - e.touches[1].clientY;
            const distance = Math.sqrt(dx * dx + dy * dy);
            
            if (this.touchDistance > 0) {
                const delta = distance - this.touchDistance;
                if (delta > 10) {
                    this.zoomIn();
                    this.touchDistance = distance;
                } else if (delta < -10) {
                    this.zoomOut();
                    this.touchDistance = distance;
                }
            }
        } else if (e.touches.length === 1 && this.isDragging) {
            const deltaX = e.touches[0].clientX - this.lastMouseX;
            const deltaY = e.touches[0].clientY - this.lastMouseY;
            
            this.offsetX -= deltaX;
            this.offsetY -= deltaY;
            
            this.lastMouseX = e.touches[0].clientX;
            this.lastMouseY = e.touches[0].clientY;
            
            this.render();
        }
    }
    
    onTouchEnd(e) {
        this.isDragging = false;
        this.touchDistance = 0;
    }
    
    onKeyDown(e) {
        switch (e.key) {
            case 'ArrowUp':
                e.preventDefault();
                this.panUp();
                break;
            case 'ArrowDown':
                e.preventDefault();
                this.panDown();
                break;
            case 'ArrowLeft':
                e.preventDefault();
                this.panLeft();
                break;
            case 'ArrowRight':
                e.preventDefault();
                this.panRight();
                break;
            case '+':
            case '=':
                e.preventDefault();
                this.zoomIn();
                break;
            case '-':
            case '_':
                e.preventDefault();
                this.zoomOut();
                break;
            case 'Home':
                e.preventDefault();
                this.fitToView();
                break;
            case 'a':
            case 'A':
                if (e.ctrlKey || e.metaKey) {
                    e.preventDefault();
                    this.addAnnotation();
                }
                break;
        }
    }
    
    // ==================== Controls ====================
    
    zoomIn() {
        if (this.zoom < 8) {
            this.setZoom(this.zoom + 1);
        }
    }
    
    zoomOut() {
        if (this.zoom > 1) {
            this.setZoom(this.zoom - 1);
        }
    }
    
    setZoom(level) {
        level = Math.max(1, Math.min(8, level));
        if (level !== this.zoom) {
            this.zoom = level;
            document.getElementById('zoomSlider').value = level;
            document.getElementById('zoomLabel').textContent = level + 'x';
            updateStatus(`Zoomed to ${level}x`);
            this.render();
        }
    }
    
    panLeft() {
        this.offsetX -= 100;
        this.render();
    }
    
    panRight() {
        this.offsetX += 100;
        this.render();
    }
    
    panUp() {
        this.offsetY -= 100;
        this.render();
    }
    
    panDown() {
        this.offsetY += 100;
        this.render();
    }
    
    fitToView() {
        this.zoom = 1;
        this.offsetX = 0;
        this.offsetY = 0;
        document.getElementById('zoomSlider').value = 1;
        document.getElementById('zoomLabel').textContent = '1x';
        updateStatus('Fit to view');
        this.render();
    }
    
    // ==================== Annotations ====================
    
    addAnnotation() {
        const label = prompt('Annotation label (optional):', '');
        if (label !== null) {
            this.annotations.push({
                x: this.offsetX + this.canvas.width / 2,
                y: this.offsetY + this.canvas.height / 2,
                label: label,
                id: Date.now()
            });
            updateAnnotationCount();
            this.render();
        }
    }
    
    clearAnnotations() {
        if (confirm('Clear all annotations?')) {
            this.annotations = [];
            updateAnnotationCount();
            this.render();
        }
    }
    
    toggleAnnotations() {
        this.showAnnotations = document.getElementById('showAnnotations').checked;
        this.render();
    }
    
    toggleGrid() {
        this.showGrid = document.getElementById('showGrid').checked;
        this.render();
    }
    
    // ==================== Rendering ====================
    
    render() {
        const startTime = performance.now();
        
        // Clear canvas
        this.ctx.fillStyle = '#000';
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
        
        // Calculate visible tiles
        const tileStartX = Math.floor(this.offsetX / TILE_SIZE);
        const tileStartY = Math.floor(this.offsetY / TILE_SIZE);
        const tilesHorizontal = Math.ceil(this.canvas.width / TILE_SIZE) + 2;
        const tilesVertical = Math.ceil(this.canvas.height / TILE_SIZE) + 2;
        
        // Render tiles
        let loadingTiles = 0;
        for (let tx = 0; tx < tilesHorizontal; tx++) {
            for (let ty = 0; ty < tilesVertical; ty++) {
                const tileX = tileStartX + tx;
                const tileY = tileStartY + ty;
                
                if (tileX >= 0 && tileY >= 0) {
                    const canvasX = (tileX * TILE_SIZE) - this.offsetX;
                    const canvasY = (tileY * TILE_SIZE) - this.offsetY;
                    
                    if (!this.renderTile(tileX, tileY, canvasX, canvasY)) {
                        loadingTiles++;
                    }
                }
            }
        }
        
        // Show loading indicator if needed
        if (loadingTiles > 0) {
            document.getElementById('loadingIndicator').style.display = 'block';
        } else {
            document.getElementById('loadingIndicator').style.display = 'none';
        }
        
        // Draw grid if enabled
        if (this.showGrid) {
            this.drawGrid(tileStartX, tileStartY, tilesHorizontal, tilesVertical);
        }
        
        // Draw annotations
        if (this.showAnnotations) {
            this.drawAnnotations();
        }
        
        // Update performance metrics
        const endTime = performance.now();
        this.lastRenderTime = endTime - startTime;
        updateMemoryInfo(this.tileCache.size);
        
        // Update UI
        updateZoomInfo(this.zoom);
        updatePositionInfo(Math.round(this.offsetX), Math.round(this.offsetY));
    }
    
    renderTile(tileX, tileY, canvasX, canvasY) {
        const cacheKey = `${this.currentSlide}-${this.zoom}-${tileX}-${tileY}`;
        
        if (this.tileCache.has(cacheKey)) {
            const img = this.tileCache.get(cacheKey);
            this.ctx.drawImage(img, canvasX, canvasY, TILE_SIZE, TILE_SIZE);
            return true;
        }
        
        // Load from server
        const url = `${BASE_URL}/${this.currentSlide}/${this.zoom}/${tileX}/${tileY}.jpg`;
        const img = new Image();
        img.crossOrigin = 'anonymous';
        
        img.onload = () => {
            // Manage cache size
            if (this.tileCache.size >= this.maxCacheSize) {
                const firstKey = this.tileCache.keys().next().value;
                this.tileCache.delete(firstKey);
            }
            
            this.tileCache.set(cacheKey, img);
            this.render(); // Re-render with loaded tile
        };
        
        img.onerror = () => {
            // Draw placeholder
            this.ctx.fillStyle = '#333';
            this.ctx.fillRect(canvasX, canvasY, TILE_SIZE, TILE_SIZE);
            
            // Draw error indicator
            this.ctx.fillStyle = '#666';
            this.ctx.font = '10px Arial';
            this.ctx.fillText(`Error: ${tileX},${tileY}`, canvasX + 5, canvasY + 15);
        };
        
        img.src = url;
        
        return false; // Still loading
    }
    
    drawGrid(startX, startY, horizontalCount, verticalCount) {
        this.ctx.strokeStyle = 'rgba(100, 200, 255, 0.3)';
        this.ctx.lineWidth = 1;
        
        for (let x = 0; x <= horizontalCount; x++) {
            const px = (startX + x) * TILE_SIZE - this.offsetX;
            this.ctx.beginPath();
            this.ctx.moveTo(px, 0);
            this.ctx.lineTo(px, this.canvas.height);
            this.ctx.stroke();
        }
        
        for (let y = 0; y <= verticalCount; y++) {
            const py = (startY + y) * TILE_SIZE - this.offsetY;
            this.ctx.beginPath();
            this.ctx.moveTo(0, py);
            this.ctx.lineTo(this.canvas.width, py);
            this.ctx.stroke();
        }
        
        // Draw coordinates
        this.ctx.fillStyle = 'rgba(100, 200, 255, 0.5)';
        this.ctx.font = '10px monospace';
        for (let x = 0; x < horizontalCount; x++) {
            for (let y = 0; y < verticalCount; y++) {
                const px = (startX + x) * TILE_SIZE - this.offsetX + 5;
                const py = (startY + y) * TILE_SIZE - this.offsetY + 15;
                if (px > 0 && py > 0 && px < this.canvas.width && py < this.canvas.height) {
                    this.ctx.fillText(`${startX + x},${startY + y}`, px, py);
                }
            }
        }
    }
    
    drawAnnotations() {
        this.annotations.forEach(ann => {
            const x = ann.x - this.offsetX;
            const y = ann.y - this.offsetY;
            
            // Draw circle
            this.ctx.fillStyle = 'rgba(255, 0, 0, 0.7)';
            this.ctx.beginPath();
            this.ctx.arc(x, y, 10, 0, Math.PI * 2);
            this.ctx.fill();
            
            // Draw border
            this.ctx.strokeStyle = 'white';
            this.ctx.lineWidth = 2;
            this.ctx.stroke();
            
            // Draw label
            if (ann.label) {
                this.ctx.fillStyle = 'rgba(0, 0, 0, 0.8)';
                this.ctx.fillRect(x + 15, y - 15, ann.label.length * 6 + 4, 18);
                
                this.ctx.fillStyle = 'white';
                this.ctx.font = 'bold 12px Arial';
                this.ctx.fillText(ann.label, x + 17, y - 2);
            }
        });
    }
    
    animationLoop() {
        // Could be used for smooth animations in future
        this.animationFrameId = requestAnimationFrame(() => this.animationLoop());
    }
    
    downloadScreenshot() {
        const link = document.createElement('a');
        link.href = this.canvas.toDataURL('image/png');
        link.download = `${this.currentSlide}-${this.zoom}x.png`;
        link.click();
        updateStatus('Screenshot saved');
    }
    
    destroy() {
        if (this.animationFrameId) {
            cancelAnimationFrame(this.animationFrameId);
        }
        this.tileCache.clear();
    }
}

// ==================== UI Functions ====================

function selectSlide(element) {
    const slideId = element.dataset.slide;
    
    // Update selection
    document.querySelectorAll('.slide-item').forEach(item => {
        item.classList.remove('active');
    });
    element.classList.add('active');
    
    // Load slide
    viewer.currentSlide = slideId;
    viewer.zoom = 1;
    viewer.offsetX = 0;
    viewer.offsetY = 0;
    viewer.annotations = [];
    
    document.getElementById('zoomSlider').value = 1;
    document.getElementById('zoomLabel').textContent = '1x';
    
    updateAnnotationCount();
    updateCurrentSlideInfo();
    updateStatus(`Loaded ${slideId}`);
    
    viewer.render();
}

function updateCurrentSlideInfo() {
    const slideId = viewer.currentSlide;
    const name = SLIDES[slideId] || 'Unknown';
    document.getElementById('currentSlideInfo').textContent = `${slideId} (${name})`;
}

function updateZoomInfo(zoom) {
    document.getElementById('zoomInfo').textContent = `${zoom}x`;
}

function updatePositionInfo(x, y) {
    document.getElementById('positionInfo').textContent = `${x}, ${y}`;
}

function updateAnnotationCount() {
    document.getElementById('annotationCount').textContent = viewer.annotations.length;
}

function updateMemoryInfo(cacheSize) {
    const estimatedMB = ((cacheSize * 10) / 1024).toFixed(1);
    document.getElementById('memoryUsage').textContent = `Memory: ${estimatedMB} MB`;
}

function updateStatus(message) {
    document.getElementById('statusText').textContent = message;
}


let viewer;

document.addEventListener('DOMContentLoaded', () => {
    viewer = new HistologyViewer('slideCanvas');
    
    // Select first slide
    const firstSlideItem = document.querySelector('.slide-item');
    if (firstSlideItem) {
        firstSlideItem.click();
    }
    
    // Cleanup on page unload
    window.addEventListener('beforeunload', () => {
        viewer.destroy();
    });
});