from dataclasses import dataclass


@dataclass(frozen=True)
class SensorInfo:
    temperature: str
    humidity: str
