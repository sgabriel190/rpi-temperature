function getCurrentTime() {
    var d = new Date();
    document.getElementById("local_time").innerHTML = "Time:" + d.toLocaleTimeString();
}

setInterval(getCurrentTime, 1000);