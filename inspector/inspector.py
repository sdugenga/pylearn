"""Inspects and displays everything knowable about a python object in a readable way.

TODO: More in depth description of what the module does (is it a module)?

TODO: Typical usage example:
    
    inspector(object)
"""

import sys


def main():
    pass

def get_identity(obj: Any) -> dict:
    """Take any object and return a dictionary of its identity properties.

    Returns:
        A dict containing the identity properties of the object.
            id: the memory address of the object as an integer.
            ref_count: the number of references to the object.
            size: the size of the object in bytes.
    """
    # No error cases as internal function.
    return {
            'id': id(obj),
            'ref_count': sys.getrefcount(obj),
            'size': obj.__sizeof__()
           }


def get_type_info(obj: Any) -> dict:
    """Take any object and return a dictionary of it's type properties.

    Returns:
        A dict containing the type properties of the object:

            type: The name of type of the object as a string (e.g 'str')

            mutable: Whether the object type is mutable or not (e.g. 'True')

            hierarchy: The type hierarchy of the object as a list from most specific
            to most general (e.g. [int, object]). Retrieved from __mro__ attribute
            which gives a tuple of the object type, or it's method resolution order.
    """
    # No error cases as internal function.
    obj_type = type(obj).__name__ # Get object type name as a string.
    
    # Check if object type is in set of immutable types:
    immutable_types =   {
                        'int',
                        'float',
                        'complex',
                        'bool',
                        'str',
                        'bytes',
                        'tuple',
                        'frozenset',
                        'NoneType',
                        }

    return {'type': obj_type,
            'mutable': obj_type not in immutable_types,
            'hierarchy': [t.__name__ for t in type(obj).__mro__]
            }


def format_address(address: int) -> str:
    """ Take memory address as an integer and return decimal and hexidecimal 
    representations.

    Raises:
        ValueError if address is not a non-zero positive integer.
    """
    if not isinstance(address, int) or isinstance(address, bool) or address <= 0:
        raise ValueError("Address is not a positive integer.")

    return f"{hex(address)} ({address})"


def display_inspection(name: str, identity: dict, type_info: dict) -> None:
    """Take information about an object and display it in a pretty format.

    Function only displays information and does not compute or return any information.

    Raises: TypeError if identity or type_info are not dicts.
            ValueError if required keys are missing from either dict.
    """
    pass


if __name__ == "__main__":
    main()
