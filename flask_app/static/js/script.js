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
    return hour + ":" +
        minutes + ":" + seconds;
}

function updateTime() {
    document.getElementById("local_time").innerHTML = "Time: " + getCurrentTime();
}

function getTemperatureValue() {
    $.post("/tempsens/get_data_json", (data) => {
        document.getElementById("local_temperature").innerHTML = "Temperature: " + data.temperature.toFixed(1);
        document.getElementById("local_humidity").innerHTML = "Humidity: " + data.humidity.toFixed(1);
        document.getElementById("sensor_status").innerHTML = "Updated with sensor data at " + getCurrentTime();
    }).fail(() => {
        document.getElementById("sensor_status").innerHTML = "FAILED to update with sensor data at " + getCurrentTime();
    });
}