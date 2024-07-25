import click
import rich
from database import create_item, create_collection


@click.group()
def create():
    """Create items and collections."""


@create.command()
@click.option('-n', '--name', type=str, help='Name of the item')
@click.option('-w', '--weight', type=int, help='Weight of the item in grams')
@click.option('-c', '--category', type=str, help='Category of the item')
@click.option('--note', type=str, help='Item note')
def item(name, weight, category, note):
    if name is None:
        name = click.prompt("Enter the name of the item", type=str)
    if weight is None:
        weight = click.prompt("Enter the weight of the item", type=int)
    if category is None:
        category = click.prompt("Enter the category of the item", type=str)
    if note is None:
        note = click.prompt("Enter a note for the item",
                            type=str, default="", show_default=False)

    # Create item
    item_id = create_item(name, weight, category, note)

    if item_id:
        rich.print(f"\n[green]Item '{name}' added successfully with ID {
                   item_id}![/green]\n")
    else:
        rich.print(f"\n[red]Item '{name}' could not be added![/red]\n")


@create.command()
@click.option('-n', '--name', type=str, help='Name of the collection')
@click.option('-d', '--description', type=str, help='Description of the collection')
@click.option('-i', '--interactive', is_flag=True, help='Interactive mode')
def collection(name, description, interactive):
    if interactive:
        name = click.prompt("Enter the name of the collection", type=str)
        description = click.prompt(
            "Enter the description of the collection", type=str)
    elif not name or not description:
        raise click.UsageError(
            "In non-interactive mode, both --name and --description must be provided.")

    collection_id = create_collection(name, description)

    rich.print(f"[green]Collection '{name}' with ID {
               collection_id} was created successfully![/green]")
