import click
from database import handle_interactive_add, add_items_to_collection


@click.group()
def add():
    """Add items to collections"""
    pass


@add.command()
@click.argument('item_ids', nargs=-1, type=int, required=False)
@click.option('-c', '--collection', 'collection_id', type=int, help='Collection ID to add items to')
@click.option('-i', '--interactive', is_flag=True, help='Interactive mode to select items and collections')
def item(item_ids, collection_id, interactive):
    """
    Add items to a collection.
    """
    if interactive:
        handle_interactive_add()
    else:
        if not item_ids:
            click.echo("You must provide at least one item ID.")
            return

        if not collection_id:
            click.echo("You must provide a collection ID.")
            return

        try:
            add_items_to_collection(collection_id, item_ids)
        except Exception as e:
            click.echo(f"An error occurred: {e}")
