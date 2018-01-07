function infiniteScroll() {
    tgt = window.scrollY+3;
    var limit = document.body.offsetHeight;
    if(tgt > limit) {
        tgt = 0 - window.innerHeight;
    }
    window.scroll(0, tgt);
}

function setBoard(table, leaders) {
    for(var i=0; i<10; i++) {
        var row = table.rows[i+1];
        if(i<leaders.length)  {
            leader = leaders[i];
            // Set the name and points
            row.cells[1].innerHTML = leader.name;
            row.cells[2].innerHTML = leader.points;
            // Set the rank
            if(i>0 && leader.points == leaders[i-1].points) {
                row.cells[0].innerHTML = table.rows[i].cells[0].innerHTML;
            } else {
                row.cells[0].innerHTML = i+1;
            }
        } else {
            // Set the cells empty
            row.cells[0].innerHTML = i+1;
            row.cells[1].innerHTML = "<i><font color='gray'>Empty</font></i>";
            row.cells[2].innerHTML = "<i><font color='gray'>N/A</font></i>";
        }
    }
}

function getLeaders() {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "/api/leaderboard", true);
    xhr.onload = function(e) {
        var response = JSON.parse(xhr.responseText);
        setBoard(document.getElementById('brideTeam'), response.topBrides);
        setBoard(document.getElementById('groomTeam'), response.topGrooms);
        setBoard(document.getElementById('mostSocial'), response.topSocial);
        setBoard(document.getElementById('mostConvert'), response.topFlipped);
    }
    xhr.send(null);
}

window.onload = function(e) {
    setInterval(infiniteScroll, 16);
    setInterval(getLeaders, 30000);
    getLeaders();
}
