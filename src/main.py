import os

import click

from command.add import add
from command.checklist import checklist
from command.create import create
from command.delete import delete
from command.list import list
from command.remove import remove
from command.view import view
from config import get_database_path
from initialize_database import create_database_schema


def initialize_database(db_path):
    """Initialize the database with the required schema if it does not exist."""
    if not os.path.exists(db_path):
        create_database_schema(db_path)


# Main CLI function
@click.group()
def cli():
    # Define the path for the SQLite database
    db_path = get_database_path()
    # Initialize database if necessary
    initialize_database(db_path)


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
