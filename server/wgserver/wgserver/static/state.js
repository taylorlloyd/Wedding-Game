brideColor = "#ff7f7f";
groomColor = "#4286f4";
updateTime= 10*1000; // 10 seconds
showTime = 10*60*1000; // 10 min
maxCols = showTime/updateTime;
data = [0.5, 0.5, 0.5];

function drawGraph(performance, canvas) {
    columns = Math.min(maxCols, performance.length)
    width = canvas.width;
    height = canvas.height;
    ctx = canvas.getContext('2d');
    colWidth = Math.ceil(width/(columns-1));
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
    drawGraph(data, canvas);
}

function updateGraph() {
    var req = new XMLHttpRequest();
    req.open("GET", "/api/ratio", false)
    req.send(null);
    var response = JSON.parse(req.responseText);
    console.log(response);
    b_pct = response.bride_side/(response.bride_side+response.groom_side);
    g_pct = 1 - b_pct;
    if(response.bride_side + response.groom_side > 0)
        data.push(response.bride_side/(response.bride_side+response.groom_side));
    drawGraph(data, document.getElementById('canvas'));
    document.getElementById('bridePct').innerHTML = (b_pct*100).toFixed(0);
    document.getElementById('groomPct').innerHTML = (g_pct*100).toFixed(0);
}

window.onload = function(e) {
    window.addEventListener('resize', resizeCanvas, false);
    resizeCanvas();
    setInterval(updateGraph,updateTime);
    updateGraph();
}
