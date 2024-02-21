import logging
from libs.models import SensorInfo
from libs import sensor

logging.basicConfig(
    format="[%(asctime)s][%(filename)s][%(levelname)8s] - %(message)s",
    level=logging.INFO,
)

LOG = logging.getLogger(__name__)


def get_sensor_info() -> SensorInfo:
    """
    Retrieve the DHT sensor values: temperature and humidity.

    Returns:
        SensorInfo: Dataclass which contains temperature and humidity key/value.
    """
    LOG.info("Getting the sensor values.")
    data = SensorInfo(temperature=sensor.temperature, humidity=sensor.humidity)
    LOG.info("Temperature:%s Humidity:%s", data.temperature, data.humidity)
    return data
