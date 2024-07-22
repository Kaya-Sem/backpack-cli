import click
import rich
from dataobjects import Collection
from collection import print_collections, print_collection_view
from item import print_items, print_item_view
import sys
from database import get_collections, get_collection, get_items, get_item


@click.group()
def view():
    """View items and collections."""
    pass


@view.command()
@click.argument("id", required=False, type=int)
def collection(id):
    if id is None:
        collections = get_collections()
        if collections:
            rich.print(f"\nAvailable collections [dim]({len(collections)})[/dim]:\n")
            print_collections(collections)
        else:
            click.echo("No collections found in the database")

        id = click.prompt("Enter the ID of the collection you want to view", type=int)

    try:
        col: Collection = get_collection(id)
        print_collection_view(col)
    except ValueError as e:
        click.echo(str(e))


@view.command()
@click.argument("id", required=False, type=int)
def item(id):
    if id is None:
        items = get_items()
        if items:
            click.echo("Available items:")
            print_items(items)
        else:
            click.echo("No items found in the database.")
            sys.exit()

        id = click.prompt("Enter the ID of the item you want to view", type=int)

    try:
        item = get_item(id)
        print_item_view(item)
    except ValueError as e:
        click.echo(str(e))
