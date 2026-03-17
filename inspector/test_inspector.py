import pytest

from inspector import (
        get_identity,
        get_type_info,
        format_address
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
        assert format_address(140153875566800) == "0x7f781df790d0 (140153875566800)"

    @pytest.mark.parametrize("obj", [-1, 0, True, 3.14, "Hello, World!"])
    def test_error_raising(self, obj):
        with pytest.raises(ValueError, match="positive integer"):
            format_address(obj)
