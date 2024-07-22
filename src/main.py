import click

from command.add import add
from command.checklist import checklist
from command.list import list
from command.remove import remove
from command.view import view
from command.create import create
from command.delete import delete


@click.group()
def cli():
    pass


# Register command from command directory
cli.add_command(checklist)
cli.add_command(add)
cli.add_command(remove)
cli.add_command(list)
cli.add_command(view)
cli.add_command(create)
cli.add_command(delete)

if __name__ == "__main__":
    cli()
