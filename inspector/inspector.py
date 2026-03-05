"""Inspects and displays everything knowable about a python object in a readable way.

TODO: More in depth description of what the module does (is it a module)?

TODO: Typical usage example:
    
    inspector(object)
"""

import sys


def main():
    pass

def get_identity(obj: Any) -> dict:
    """    
    Take any object and return a dictionary of its identity properties.

    Returns:
        A dict containing the identity properties of the object.
            id: the memory address of the object as an integer.
            ref_count: the number of references to the object.
            size: the size of the object in bytes.
    """
    return {
            'id': id(obj),
            'ref_count': sys.getrefcount(obj),
            'size': obj.__sizeof__()
           }


def get_type_info(obj: Any) -> dict:
    """
    Take any object and return a dictionary of it's type properties.

    Returns:
        A dict containing the type properties of the object:
            type: The name of type of the object as a string (e.g 'str')
            mutable: Whether the object type is mutable or not (e.g. 'yes')
            hierarchy: The type hierarchy of the object as a list from most specific
            to most general (e.g. [int, object]) # I think!
    """
    pass

if __name__ == "__main__":
    main()

