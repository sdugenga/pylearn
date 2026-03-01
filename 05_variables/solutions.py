from typing import Any, Tuple


def main():
    pass


def get_type_name(value: Any) -> str:
    """Take any value and return its type name as a string"""
    return type(value).__name__

def same_type(a: Any, b: Any) -> bool:
    """Take any two values and assess whether they are the same type"""
    return type(a) == type(b)


def is_truthy(value: Any)-> bool:
    """Take any value and return whether it is 'truthy' or not."""
    return bool(value)


def compare_identity(a: Any, b: Any) -> tuple:
    """Take two values and return a tuple of three booleans comparing
    whether the values are equal in value, whether they are the same
    object and whether they share the same memory address."""
    return (a == b, a is b, id(a) == id(b))


def is_none(value: Any) -> bool:
    """Take a value and check whether that value is None"""
    return value is None


def mutability_comparison() -> tuple:
    """Demonstrate that integer assignment creates independent values,
    list assignment maintains a shared value, changing a list which is
    a mutable value does change the shared list."""
    # should create two independent values
    int_a = 50
    int_b = int_a
    int_b = 100
    # should change the original list
    list_a = [4, 5, 6]
    list_b = list_a
    list_b[2] = 99

    return (int_a == 100, list_b[2] == 99)


if __name__ == "__main__":
    main()
