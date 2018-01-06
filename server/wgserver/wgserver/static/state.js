brideColor = "#ff7f7f";
groomColor = "#4286f4";
lastData = [];

function drawGraph(performance, canvas) {
    lastData = performance;
    columns = Math.min(33, performance.length)
    width = canvas.width;
    height = canvas.height;
    ctx = canvas.getContext('2d');
    colWidth = Math.floor(width/(columns-1));
    // Draw each column
    base=performance.length-columns;
    for(i=0; i<columns-1; i++) {
        drawColumn(ctx, i*colWidth, colWidth, height, performance[base+i], performance[base+i+1]);
    }
}
function drawColumn(ctx, x_off, width, height, start, end) {
    // Fill rects
    lower = Math.max(start, end);
    split = Math.floor(lower*height);
    ctx.fillStyle = brideColor;
    ctx.fillRect(x_off, 0, width,split);
    ctx.fillStyle = groomColor;
    ctx.fillRect(x_off, split, width, height-(split));

    // Draw triangle
    ctx.beginPath();
    ctx.moveTo(x_off, split);
    ctx.lineTo(x_off, Math.floor(start*height));
    ctx.lineTo(x_off+width, Math.floor(end*height));
    ctx.lineTo(x_off+width, split);
    ctx.fill();
}

function resizeCanvas() {
    var canvas = document.getElementById('canvas');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    drawGraph(lastData, canvas);
}

window.onload = function(e) {
    window.addEventListener('resize', resizeCanvas, false);
    resizeCanvas();
    perf = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.5, 0.4, 0.3, 0.6, 0.9, 1.0];
    drawGraph(perf, document.getElementById('canvas'));
}
