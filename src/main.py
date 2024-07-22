import click

from commands.add import add
from commands.checklist import checklist
from commands.list import list
from commands.remove import remove
from commands.view import view
from commands.create import create
from commands.delete import delete


@click.group()
def cli():
    pass


# Register commands from commands directory
cli.add_command(checklist)
cli.add_command(add)
cli.add_command(remove)
cli.add_command(list)
cli.add_command(view)
cli.add_command(create)
cli.add_command(delete)

if __name__ == "__main__":
    cli()
