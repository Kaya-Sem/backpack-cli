from typing import List, Dict
import rich

import term_piechart  # https://github.com/va-h/term-piechart


# Format data correctly for piechart -> {"name": name, "value": value}
def get_pie_data(weights: Dict[str, float]) -> List[dict]:
    # Determine max length category to determine width.
    max_len = max(len(category) for category in weights.keys())
    return [
        {"name": f"{category.ljust(max_len + 5)} {format_weight(int(weight))}", "value": int(weight)}
        for category, weight in weights.items()
    ]


def generate_chart(data: List[dict]):
    pie = term_piechart.Pie(
        data,
        radius=4,
        autocolor=True,
        autocolor_pastel_factor=0.0,
        legend={"line": 0, "format": "{percent:>5.0f}% {label} {name:<10} "},
    )
    return pie


def print_collection_view(collection):
    rich.print(f"\n≡ [bold]{collection.name}[/bold]")
    rich.print(f"  [italic]{collection.description}[/italic]\n")

    data = get_pie_data(collection.get_category_weights())
    print(generate_chart(data))

    total_weight = format_weight(collection.get_total_weight())
    print(f"Total weight: {total_weight}\n")

    for category, items_list in collection.items.items():
        rich.print(f"[dim]{category}[/dim]")
        print_collection_items(items_list)
        print()


def print_collection_items(items):
    max_name_len = max(len(item.name) for item in items)
    max_note_len = max(len(item.note) for item in items)
    padding = 10

    for item in items:
        formatted_weight = format_weight(item.weight)
        name = f"[bold]{item.name.ljust(max_name_len + padding)}[/bold]"
        note = f"[italic]{item.note.ljust(max_note_len + padding)}[/italic]"
        weight = f"[blue]{formatted_weight}[/blue]"

        rich.print(f"{name} {note} {weight}")


class Collection:
    def __init__(
            self,
            id,
            name,
            desc,
            items
    ):
        self.id = id
        self.name = name
        self.description = desc
        self.items = items

    def get_category_weights(self) -> Dict[str, float]:
        return {category: sum(item.weight for item in item_list) for category, item_list in self.items.items()}

    def get_total_weight(self) -> int:
        return sum(sum(item.weight for item in item_list) for _, item_list in
                   self.items.items())


def print_collections(collections: List[Collection]):
    for collection in collections:
        rich.print(
            f"[dim]{collection.id}[/dim] [bold]{collection.name}[/bold] [italic]{collection.description}[/italic]")


# format weight in grams
def format_weight(weight):
    return f"{weight / 1000:.1f} kg" if weight >= 1000 else f"{int(weight)} g"
