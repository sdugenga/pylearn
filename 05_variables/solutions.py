from typing import Any


def main():
    pass


def get_type_name(value: Any) -> str:
    """Take any value and return its type name as a string"""
    return type(value).__name__

def same_type(a: Any, b: Any) -> bool:
    """Take any two values and assess whether they are the same type"""
    return type(a) == type(b)

if __name__ == "__main__":
    main()
