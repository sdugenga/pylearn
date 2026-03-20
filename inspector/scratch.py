from inspector import get_identity, get_type_info, format_address
from rich.console import Console, Group
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

IMMORTAL_SENTINEL = 0xC0000000
console = Console(width=88)


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
    if not type_info['mutable']:
        mutability = f"[on green]Immutable"

    # Format the hierarchy list:
    hierarchy = Text()
    for item in type_info['hierarchy']:
        hierarchy.append(str(item), style="cyan")
        if item != type_info['hierarchy'][-1]:
            hierarchy.append(" -> ", style="white")

    # Put the tables together
    type_table = Table(box=None, title="Type Info:", show_header=True, title_justify="full", title_style="u")

    type_table.add_column(justify="right", style="bold")
    type_table.add_column(justify="left")

    type_table.add_row("Type:", f"[cyan]{type_info['type']}[/cyan]")
    type_table.add_row("Object Hierarchy:", hierarchy)
    type_table.add_row("Mutability:", mutability)

    id_table = Table(box=None, title="Identity:", show_header=True, title_justify="full", title_style="u")

    id_table.add_column(justify="right", style="bold")
    id_table.add_column(justify="left")

    id_table.add_row("Reference Count:", str(ref_count))
    id_table.add_row("Size:", f"{identity['size']} B")
    id_table.add_row(
        "ID:",
        f"[#569CD6]0x[/#569CD6]"
        f"[#B5CEA8]{hex_address}[/#B5CEA8]"
        f" ({dec_address})"
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
            padding=(1, 0, 1, 1)
        )
    )


def main():
    banana = 5

    banana_identity = get_identity(banana)
    banana_type = get_type_info(banana)

    banana_name = "banana"

    display_inspection(banana_name, banana_identity, banana_type)


if __name__ == "__main__":
    main()
