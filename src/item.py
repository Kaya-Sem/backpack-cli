from typing import List

from collection import format_weight
import rich

from dataobjects import Item


def print_item_view(item: Item):
    label_width = 10
    rich.print(f"\n> [bold]{item.name}[/bold]")
    rich.print(f"  [italic]{item.note}[/italic]\n")
    rich.print(f"[dim]{'weight:'.ljust(label_width)}[/dim] {format_weight(item.weight)}")
    rich.print(f"[dim]{'category:'.ljust(label_width)}[/dim] {item.category}")


def print_items(items: List[Item]):
    for item in items:
        rich.print(f"[dim]{item.id}[/dim] [bold]{item.name}[/bold]")
