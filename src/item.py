from typing import List

from collection import format_weight
import rich


class Item:
    def __init__(
            self,
            item_id: int,
            name: str,
            weight: float,
            note: str,
            category: str,
    ):
        self.id = item_id
        self.name = name
        self.weight = weight
        self.note = note
        self.category = category

    def __str__(self):
        return f"{self.id}: {self.name}, {self.weight}"


def print_item_view(item: Item):
    label_width = 15
    rich.print(f"\n[bold]{item.name}[/bold]")
    rich.print(f"[dim]{'note:'.ljust(label_width)}[/dim]  [italic]{item.note}[/italic]")
    rich.print(f"[dim]{'weight:'.ljust(label_width)}[/dim] {format_weight(item.weight)}")
    rich.print(f"[dim]{'category:'.ljust(label_width)}[/dim] {item.category}")


def print_items(items: List[Item]):
    for item in items:
        rich.print(f"[dim]{item.id}[/dim] [bold]{item.name}[/bold]")
