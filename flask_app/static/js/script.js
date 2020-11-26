function getCurrentTime() {
    let date = new Date();
    let hour = date.getHours();
    let minutes = date.getMinutes();
    let seconds = date.getSeconds();
    if (minutes < 10) {
        minutes = "0" + minutes;
    }
    if (seconds < 10) {
        seconds = "0" + seconds;
    }
    if (hour < 10) {
        hour = "0" + hour;
    }
    document.getElementById("local_time").innerHTML = "Time: " +
        hour + ":" +
        minutes + ":" +
        seconds;
}

function getTemperatureValue() {
    $.post("/tempsens/get_data_json", (data, status) => {
        document.getElementById("local_temperature").innerHTML = "Temperature: " + data.temp.toFixed(1);
        document.getElementById("local_humidity").innerHTML = "Humidity: " + data.hum.toFixed(1);
    });
}