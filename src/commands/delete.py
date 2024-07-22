import click
import rich
import sys
from database import get_items, delete_item, get_collections, delete_collection


@click.group()
def delete():
    """Delete items and collections."""
    pass


#  TODO: use print items instead
@delete.command()
@click.argument("id", required=False, type=int)
def item(id):
    if id is None:
        items = get_items()
        if items:
            print(f"{len(items)} available items:")
            for item in items:
                print(f"[dim]{item.id}:[/dim] {item.name}")
        else:
            print("No items found in the database.")
            sys.exit()

        id = click.prompt("Enter the ID of the item you want to delete", type=int)

    try:
        delete_item(id)
    except ValueError as e:
        click.echo(str(e))


@delete.command()
@click.argument("id", required=False, type=int)
def collection(id):
    if id is None:
        collections = get_collections()
        if collections:
            print(f"{len(collections)} available collections:")
            for collection in collections:
                print(f"[dim]{collection.id}:[/dim] {collection.name}")
        else:
            print("\nNo collections found in the database.\n")
            sys.exit()

        id = click.prompt("Enter the ID of the collection you want to delete", type=int)

    try:
        delete_collection(id)
        rich.print(f"\n[green]Collection with ID {id} was succesfully removed[/green]\n")
    except ValueError as e:
        click.echo(str(e))
