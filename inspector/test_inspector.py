import sys

import pytest
from rich.console import Console

from inspector import (
        get_identity,
        get_type_info,
        format_address,
        display_inspection
        )


def param_add(a, b):  # Dummy function to run parametrized tests on functions.
    return a + b


class TestParamGetIdentity:

    @pytest.mark.parametrize("obj", [
                                        5,
                                        "Hello, World!",
                                        3.14,
                                        [1, 2, 3],
                                        param_add
                                     ]
                             )
    def test_param_get_identity(self, obj):
        test_dict = get_identity(obj)
        assert isinstance(test_dict['id'], int) and test_dict['id'] > 0
        assert isinstance(test_dict['ref_count'], int) and test_dict['ref_count'] > 0
        assert isinstance(test_dict['size'], int) and test_dict['size'] > 0


class TestGetTypeInfo:

    @pytest.mark.parametrize("obj", ["Hello, World!", 3.14, 42, (1, 2, 3)])
    def test_immutability(self, obj):
        test_type_dict = get_type_info(obj)
        assert not test_type_dict['mutable']

    @pytest.mark.parametrize("obj", [
                                        [1, 2, 3],
                                        {'i': 1, 'ii': 2, 'iii': 3},
                                        {1, 2, 3}
                                    ]
                             )
    def test_mutability(self, obj):
        test_type_dict = get_type_info(obj)
        assert test_type_dict['mutable']

    def test_hierarchy(self):
        test_bool = True
        test_type_dict = get_type_info(test_bool)
        assert test_type_dict['hierarchy'] == ['bool', 'int', 'object']

    @pytest.mark.parametrize("obj", ["Hello, World!", True, [1, 2, 3], 42, param_add])
    def test_hierarchy_object(self, obj):
        test_type_dict = get_type_info(obj)
        assert test_type_dict['hierarchy'][-1] == 'object'


class TestFormatAddress:

    def test_positive_integer(self):
        assert format_address(140153875566800) == {
            "hex": "0x7f781df790d0",
            "dec": "140153875566800"
            }

    @pytest.mark.parametrize("obj", [-1, 0, True, 3.14, "Hello, World!"])
    def test_error_raising(self, obj):
        with pytest.raises(ValueError, match="positive integer"):
            format_address(obj)


class TestDisplayInspection:

    valid_id_dict = {
        "id": id(42),
        "ref_count": sys.getrefcount(42),
        "size": (42).__sizeof__
        }
    
    valid_type_dict = {
        "type": "int",
        "mutable": False,
        "hierarchy": ["int", "object"]
        }
    
    def test_raises_type_error_for_non_dict_id(self):
        with pytest.raises(TypeError):
            display_inspection("x", "not a dict", self.valid_type_dict)

    def test_raises_type_error_for_non_dict_type(self):
        with pytest.raises(TypeError):
            display_inspection("x", self.valid_id_dict, "not a dict")

    def test_raises_value_error_for_missing_id_keys(self):
        with pytest.raises(ValueError):
            display_inspection("x", {"id": 123}, self.valid_type_dict)

    def test_raises_value_error_for_missing_type_keys(self):
        with pytest.raises(ValueError):
            display_inspection("x", self.valid_id_dict, {"type": "int"})

    def test_produces_output_for_valid_input(self):
        from io import StringIO
        buffer = StringIO()
        test_console = Console(file=buffer, force_terminal=True, width=100)
        display_inspection("x", self.valid_id_dict, self.valid_type_dict, test_console)
        output = buffer.getvalue()
        assert len(output) > 0