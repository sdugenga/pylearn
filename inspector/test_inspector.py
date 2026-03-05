import pytest

from inspector import (
        get_identity,
        )


def param_add(a, b): # Dummy function to run parametrized tests on functions.
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

    # TODO: Test mutability for two immutable types.
    # TODO: Test mutability for two mutable types.
    # TODO: Test hierarchy for bool ('bool', 'int', 'object').
    # TODO: Test that object always appears as last item in hierarchy (-1).
