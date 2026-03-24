import copy
import functools
import time
from typing import Any, Callable


# Sample dataset:
SAMPLE_READINGS = [
    {
        "id": "S01",
        "zone": "Zone1",
        "type": "temperature",
        "value": 21.3,
        "unit": "C",
        "timestamp": "2024-01-15T09:00",
    },
    {
        "id": "S02",
        "zone": "Zone1",
        "type": "co2",
        "value": 623.0,
        "unit": "ppm",
        "timestamp": "2024-01-15T09:00",
    },
    {
        "id": "S03",
        "zone": "Zone1",
        "type": "humidity",
        "value": 47.0,
        "unit": "%",
        "timestamp": "2024-01-15T09:00",
    },
    {
        "id": "S04",
        "zone": "Zone2",
        "type": "temperature",
        "value": 19.8,
        "unit": "C",
        "timestamp": "2024-01-15T09:00",
    },
    {
        "id": "S05",
        "zone": "Zone2",
        "type": "co2",
        "value": 890.0,
        "unit": "ppm",
        "timestamp": "2024-01-15T09:00",
    },
    {
        "id": "S06",
        "zone": "Zone2",
        "type": "lux",
        "value": 320.0,
        "unit": "lux",
        "timestamp": "2024-01-15T09:00",
    },
    {
        "id": "S07",
        "zone": "Zone3",
        "type": "temperature",
        "value": 26.1,
        "unit": "C",
        "timestamp": "2024-01-15T09:15",
    },
    {
        "id": "S08",
        "zone": "Zone3",
        "type": "co2",
        "value": 1200.0,
        "unit": "ppm",
        "timestamp": "2024-01-15T09:15",
    },
    {
        "id": "S09",
        "zone": "Zone3",
        "type": "humidity",
        "value": None,
        "unit": "%",
        "timestamp": "2024-01-15T09:15",
    },
    {
        "id": "S10",
        "zone": "Zone1",
        "type": "temperature",
        "value": -999.0,
        "unit": "C",
        "timestamp": "2024-01-15T09:30",
    },
    {
        "id": "S01",
        "zone": "Zone1",
        "type": "temperature",
        "value": 21.3,
        "unit": "C",
        "timestamp": "2024-01-15T09:00",
    },
    {
        "id": "S11",
        "zone": "Zone2",
        "type": "temperature",
        "value": 22.5,
        "unit": "F",
        "timestamp": "2024-01-15T09:30",
    },
]

# Valid measurement ranges — used for outlier detection
VALID_RANGES = {
    "temperature": (-10.0, 50.0),
    "co2": (300.0, 5000.0),
    "humidity": (0.0, 100.0),
    "lux": (0.0, 100000.0),
}

# Comfort thresholds — used for anomaly flagging
COMFORT_THRESHOLDS = {
    "temperature": (18.0, 26.0),
    "co2": (0.0, 1000.0),
    "humidity": (30.0, 70.0),
    "lux": (100.0, 2000.0),
}


def main():
    pass


def parse_reading(raw: dict) -> dict:
    """Takes raw data and validates the data structure.

        Args:
            raw (dict): The raw reading dictionary.

        Returns:
            dict: A shallow copy of the input dictionary if all required keys present.

        Required keys:
            id, zone, type, value, unit, timestamp

        Raises:
            ValueError on any missing keys, listing the missing keys.
    """
    validated_copy = copy.copy(raw)
    required_keys = {"id", "zone", "type", "value", "unit", "timestamp"}
    actual_keys = set(validated_copy.keys())
    missing_keys = required_keys - actual_keys

    if missing_keys:
        missing_str = ", ".join(sorted(missing_keys))
        raise ValueError(f"Missing required keys: {missing_str}")

    return validated_copy


if __name__ == "__main__":
    main()
