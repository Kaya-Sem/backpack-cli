import click
import rich
import sys
from database import get_items, delete_item, get_collections, delete_collection


@click.group()
def delete():
    """Delete items and collections."""


#  TODO: use print items instead
@delete.command()
@click.argument("item_id", required=False, type=int)
def item(item_id):
    if item_id is None:
        items = get_items()
        if items:
            print(f"{len(items)} available items:")
            for item in items:
                print(f"[dim]{item.id}:[/dim] {item.name}")
        else:
            print("No items found in the database.")
            sys.exit()

        item_id = click.prompt("Enter the ID of the item you want to delete", type=int)

    try:
        delete_item(item_id)
    except ValueError as e:
        click.echo(str(e))


@delete.command()
@click.argument("collection_id", required=False, type=int)
def collection(collection_id):
    if collection_id is None:
        collections = get_collections()
        if collections:
            print(f"{len(collections)} available collections:")
            for collection in collections:
                print(f"[dim]{collection.id}:[/dim] {collection.name}")
        else:
            print("\nNo collections found in the database.\n")
            sys.exit()

        collection_id = click.prompt("Enter the ID of the collection you want to delete", type=int)

    try:
        delete_collection(collection_id)
        rich.print(f"\n[green]Collection with ID {collection_id} was succesfully removed[/green]\n")
    except ValueError as e:
        click.echo(str(e))
