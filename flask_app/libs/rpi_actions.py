import logging
from libs.models import SensorInfo
from libs import sensor

logging.basicConfig(
    format="[%(asctime)s][%(filename)s][%(levelname)8s] - %(message)s",
    level=logging.INFO,
)

LOG = logging.getLogger(__name__)

def retry(max_retries):
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            if retries < max_retries:
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as _:
                    retries += 1
            else:
              raise Exception(f"Max retries of function {func} exceeded")
        return wrapper
    return decorator

@retry(max_retries=5)
def get_sensor_info() -> SensorInfo:
    """
    Retrieve the DHT sensor values: temperature and humidity.

    Returns:
        SensorInfo: Dataclass which contains temperature and humidity key/value.
    """
    LOG.info("Getting the sensor values.")
    data = SensorInfo(
        temperature=round(float(sensor.temperature), 1),
        humidity=round(float(sensor.humidity), 1)
    )
    LOG.info("Temperature:%s Humidity:%s", data.temperature, data.humidity)
    return data
