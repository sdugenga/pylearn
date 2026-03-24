import pytest

from solutions import parse_reading


class TestParseReading:
    valid_reading = {
        "id": "S01",
        "zone": "Zone1",
        "type": "temperature",
        "value": 21.3,
        "unit": "C",
        "timestamp": "2024-01-15T09:00",
    }

    one_missing_key = {
        "id": "S01",
        "type": "temperature",
        "value": 21.3,
        "unit": "C",
        "timestamp": "2024-01-15T09:00",
    }

    multiple_missing_keys = {
        "id": "S01",
        "type": "temperature",
        "value": 21.3,
        "timestamp": "2024-01-15T09:00",
    }

    empty_dict = {}

    def test_valid_reading(self):
        validated_data = parse_reading(self.valid_reading)
        assert validated_data == self.valid_reading

    def test_one_missing_key(self):
        with pytest.raises(ValueError) as e:
            parse_reading(self.one_missing_key)
        assert str(e.value) == "Missing required keys: zone"

    def test_multiple_missing_keys(self):
        with pytest.raises(ValueError) as e:
            parse_reading(self.multiple_missing_keys)
        assert str(e.value) == "Missing required keys: unit, zone"

    def test_empty_dict(self):
        with pytest.raises(ValueError) as e:
            parse_reading(self.empty_dict)
        assert (
            str(e.value)
            == "Missing required keys: id, timestamp, type, unit, value, zone"
        )

    def test_for_copy(self):
        validated_data = parse_reading(self.valid_reading)
        assert id(validated_data) is not id(self.valid_reading)
