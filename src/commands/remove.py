import click
from database import handle_interactive_remove, remove_items_from_collection


@click.group()
def remove():
    """Remove items from collections"""
    pass


@remove.command()
@click.argument('item_ids', nargs=-1, type=int, required=False)
@click.option('-c', '--collection', 'collection_id', type=int, help='Collection ID to remote items from')
@click.option('-i', '--interactive', is_flag=True, help='Interactive mode to select items and collections')
def item(item_ids, collection_id, interactive):
    """
    Remove items from a collection.
    """
    if interactive:
        handle_interactive_remove()
    else:
        if not item_ids:
            click.echo("You must provide at least one item ID.")
            return

        if not collection_id:
            click.echo("You must provide a collection ID.")
            return

        try:
            remove_items_from_collection(collection_id, item_ids)
        except Exception as e:
            click.echo(f"An error occurred: {e}")
