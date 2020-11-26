from flask import Flask, render_template, jsonify

from rpi.rpi_setup import getInfo, powerOnLed, powerOffLed, checkTemperature

app = Flask(__name__)


@app.route('/tempsens', methods=["GET"])
def tempsens_page():
    data: dict = getInfo()
    checkTemperature(data["temperature"])
    return render_template('index.html', temperature=data["temperature"], humidity=data["humidity"])


@app.route('/tempsens/get_data_json', methods=["POST"])
def get_data_json():
    data: dict = getInfo()
    return jsonify(data)


@app.route('/tempsens/power_led', methods=["POST"])
def get_data_json():
    powerOnLed()
    return jsonify(), 201


@app.route('/tempsens/disable_led', methods=["POST"])
def get_data_json():
    powerOffLed()
    return jsonify(), 201


if __name__ == "__main__":
    app.run(host="192.168.0.107", port="80")
