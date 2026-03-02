import copy
from typing import Any


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


def shallow_copy_list(lst: list) -> list:
    """Take a list and return a shallow copy of that list."""
    return copy.copy(lst)


def deep_copy_list(lst: list) -> list:
    """Take a list and return a deep copy of that list."""
    return copy.deepcopy(lst)


def to_int(value: Any) -> int:
    """
    Take a value and attempt to convert it to an integer.
    
    Raises:
        ValueError: If value cannot be converted to integer
    """
    try:
        return int(value)
    except (ValueError, TypeError) as e:
        raise ValueError(f"Cannot convert {repr(value)} to int") from e


def to_safe_string(value: Any) -> str:
    """Take any value and safely returns it as a string."""
    if value == None:
        return "null"
    else:
        return str(value)


def local_scope_demo() -> str:
    """Assigns a string to a variable, and returns that variable."""
    message = "Hello, World!"
    return message


def make_greeting(greeting: str):
    """
    Takes a string and returns a function called hello which remembers that string.
    """
    def hello(name: str) -> str:
        return(f"{greeting}, {name}!")

    return hello


if __name__ == "__main__":
    main()
