import logging
from dataclasses import asdict
from flask import Flask, render_template
from libs import HOST, PORT
from libs.rpi_actions import get_sensor_info
from libs.models import SensorInfo

logging.basicConfig(
    format="[%(asctime)s][%(filename)s][%(levelname)8s] - %(message)s",
    level=logging.INFO,
)

LOG = logging.getLogger(__name__)

app = Flask(__name__)


@app.route("/tempsens", methods=["GET"])
def tempsens_page():
    data: SensorInfo = get_sensor_info()
    return (
        render_template(
            "index.html", temperature=data.temperature, humidity=data.humidity
        ),
        200,
    )


@app.route("/tempsens/get_data_json", methods=["POST"])
def get_data_json():
    data: SensorInfo = get_sensor_info()
    return asdict(data), 200


@app.errorhandler(Exception)
def exception_handler(err):
    LOG.error(err)
    return {"message": str(err)}, 500


def main() -> None:
    """
    Entry method for the application.
    """
    app.run(host=HOST, port=PORT)


if __name__ == "__main__":
    main()
