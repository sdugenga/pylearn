import pytest

from solutions import (
    get_type_name,
    same_type,
    is_truthy,
)


class TestGetTypeName:

    def test_int(self):
        assert get_type_name(42) == "int"

    def test_str(self):
        assert get_type_name("Hello, World!") == "str"

    def test_float(self):
        assert get_type_name(3.14) == "float"

    def test_bool(self):
        assert get_type_name(True) == "bool"

    def test_none(self):
        assert get_type_name(None) == "NoneType"

    def test_string(self):
        assert isinstance(get_type_name(42), str)


class TestSameType:

    def test_true(self):
        assert same_type(1, 2) == True

    def test_false(self):
        assert same_type(1, "Hello, World!") == False

    def test_false_bool(self):
        assert same_type(True, 1) == False

    def test_bool_and_bool(self):
        assert same_type(False, True) == True


class TestTruthy:

    def test_zero(self):
        assert is_truthy(0) == False

    def test_one(self):
        assert is_truthy(1) == True

    def test_empty_string(self):
        assert is_truthy("") == False

    def test_string(self):
        assert is_truthy("Hello, World!") == True

    def test_none(self):
        assert is_truthy(None) == False

    def test_empty_list(self):
        assert is_truthy([]) == False

    def test_list(self):
        assert is_truthy([0]) == True
