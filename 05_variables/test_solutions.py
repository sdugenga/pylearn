import pytest

from solutions import (
    get_type_name,
    is_none,
    same_type,
    is_truthy,
    compare_identity,
    mutability_comparison,
    shallow_copy_list,
    deep_copy_list,
    to_int,
    to_safe_string,
    local_scope_demo,
    make_greeting,
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


class TestCompareValues:

    def test_large_integer(self):
        a = [1, 2, 3]
        b = [1, 2, 3]
        assert compare_identity(a, b) == (True, False, False)

    def test_small_integer(self):
        assert compare_identity(10, 10) == (True, True, True)


class TestIsNone:

    def test_none(self):
        assert is_none(None) == True

    def test_number(self):
        assert is_none(0) == False

    def test_bool(self):
        assert is_none(False) == False

    def test_empty_string(self):
        assert is_none("") == False


class TestMutabilityComparison:

    def test_mutability_comparison(self):
        assert mutability_comparison() == (False, True)


class TestShallowCopyList:

    def test_shallow_copy_list(self):
        lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        new_lst = shallow_copy_list(lst)
        new_lst[1][1] = 50
        assert lst[1][1] == 50

class TestDeepCopyList:

    def test_deep_copy_list(self):
        lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        new_lst = deep_copy_list(lst)
        new_lst[1][1] = 50
        assert lst[1][1] == 5


class TestToInt:

    def test_valid_string(self):
        assert to_int("42") == 42

    def test_valid_float(self):
        assert to_int(3.9) == 3

    def test_invalid_string(self):
        with pytest.raises(ValueError):
            to_int("Hello, World!")

    def test_none_raises(self):
        with pytest.raises(ValueError):
            to_int(None)

    def test_error_message(self):
        with pytest.raises(ValueError, match="Cannot convert"):
            to_int("Hello, World!")


class TestToSafeString:

    def test_integer(self):
        assert to_safe_string(42) == "42"

    def test_none_type(self):
        assert to_safe_string(None) == "null"

    def test_boolean(self):
        assert to_safe_string(True) == "True"

    def test_float(self):
        assert to_safe_string(3.14) == "3.14"

    def test_list(self):
        assert to_safe_string([1, 2, 3]) == "[1, 2, 3]"


class TestLocalScopeDemo:
        
    def test_local_scope(self):
        assert local_scope_demo() == "Hello, World!"

        with pytest.raises(NameError):
            message


class TestMakeGreeting:

    def test_alice(self):
        hello = make_greeting("Hello")
        assert hello("Alice") == "Hello, Alice!"
