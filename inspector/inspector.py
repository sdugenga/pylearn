"""Inspects and displays everything knowable about a python object in a readable way.

TODO: More in depth description of what the module does (is it a module)?

TODO: Typical usage example:

    inspector(object)
"""

import sys

from rich.console import Console, Group
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from typing import Any

# TODO(Ch06): Replace chain display with tree display after covering recursion properly.

IMMORTAL_SENTINEL = 0xC0000000
console = Console()


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
    return {"id": id(obj), "ref_count": sys.getrefcount(obj), "size": obj.__sizeof__()}


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
    obj_type = type(obj).__name__  # Get object type name as a string.

    # Check if object type is in set of immutable types:
    immutable_types = {
        "int",
        "float",
        "complex",
        "bool",
        "str",
        "bytes",
        "tuple",
        "frozenset",
        "NoneType",
    }

    return {
        "type": obj_type,
        "mutable": obj_type not in immutable_types,
        "hierarchy": [t.__name__ for t in type(obj).__mro__],
    }


def format_address(address: int) -> str:
    """Take memory address as an integer and return decimal and hexidecimal
    representations.

    Raises:
        ValueError if address is not a non-zero positive integer.
    """
    if not isinstance(address, int) or isinstance(address, bool) or address <= 0:
        raise ValueError("Address is not a positive integer.")

    return {"hex": f"{hex(address)}", "dec": f"{address}"}


def display_inspection(name: str, identity: dict, type_info: dict) -> None:
    """Take information about an object and display it in a pretty format.

    Function only displays information and does not compute or return any information.

    Raises: TypeError if identity or type_info are not dicts.
            ValueError if required keys are missing from either dict.
    """
    ref_count = identity["ref_count"]

    # Check if cached or immortal value and format
    if identity["ref_count"] == IMMORTAL_SENTINEL:
        ref_count = f"[blue]Immortal[/blue] (cached)"

    # Format the addresses
    address_info = format_address(identity["id"])
    hex_address = address_info["hex"]
    dec_address = address_info["dec"]
    hex_parts = hex_address.split("x")
    hex_address = hex_parts[1]

    # Format the mutablity string
    mutability = f"[on red]Mutable"
    if not type_info["mutable"]:
        mutability = f"[on green]Immutable"

    # Format the hierarchy list:
    hierarchy = Text()
    for item in type_info["hierarchy"]:
        hierarchy.append(str(item), style="cyan")
        if item != type_info["hierarchy"][-1]:
            hierarchy.append(" -> ", style="white")

    # Put the tables together
    type_table = Table(
        box=None,
        title="Type Info:",
        show_header=True,
        title_justify="full",
        title_style="u",
    )

    type_table.add_column(justify="right", style="bold")
    type_table.add_column(justify="left")

    type_table.add_row("Type:", f"[cyan]{type_info['type']}[/cyan]")
    type_table.add_row("Object Hierarchy:", hierarchy)
    type_table.add_row("Mutability:", mutability)

    id_table = Table(
        box=None,
        title="Identity:",
        show_header=True,
        title_justify="full",
        title_style="u",
    )

    id_table.add_column(justify="right", style="bold")
    id_table.add_column(justify="left")

    id_table.add_row("Reference Count:", str(ref_count))
    id_table.add_row("Size:", f"{identity['size']} B")
    id_table.add_row(
        "ID:",
        f"[#569CD6]0x[/#569CD6]"
        f"[#B5CEA8]{hex_address}[/#B5CEA8]"
        f" ({dec_address})",
    )

    # Group the tables
    table_group = Group(type_table, "", id_table)

    # Print the tables
    console.print(
        Panel.fit(
            table_group,
            title=f"[#9CDCFE]Inspecting: [bold]{name}[/bold][/#9CDCFE]",
            title_align="left",
            border_style="#9CDCFE",
            padding=(1, 0, 1, 1),
        )
    )


if __name__ == "__main__":
    main()
