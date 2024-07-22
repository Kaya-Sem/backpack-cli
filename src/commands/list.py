import click
import rich
from database import get_items, get_categories, get_collections
from collection import print_collections
from item import print_items


@click.group()
def list():
    """List items, collections and categories"""
    pass


@list.command()
def items():
    items = get_items()
    if items:
        rich.print(f"\nItems in the database [dim]({len(items)})[/dim]:\n")
        print_items(items)

    else:
        rich.print("\n[red]No items found in the database.[/red]\n")


@list.command()
def categories():
    categories = get_categories()
    if categories:
        rich.print("\nCategories in the database:\n")
        for category in categories:
            rich.print(f"- {category}")
    else:
        rich.print("\n[red]There are no categories in the database.[/red]\n")


@list.command()
def collections():
    collections = get_collections()
    if collections:
        rich.print(f"\nCollections in the database [dim]({len(collections)})[/dim]:\n")
        print_collections(collections)
        print()

    else:
        rich.print("\n[red]No collections found in the database[/red]\n")
