import os

import click

from click_commands.add import add
from click_commands.checklist import checklist
from click_commands.create import create
from click_commands.delete import delete
from click_commands.list import list
from click_commands.remove import remove
from click_commands.view import view
from click_commands.import_command import import_lighterpack
from click_commands.edit import edit
from config import get_database_path
from initialize_database import create_database_schema


def initialize_database(db_path):
    """Initialize the database with the schema if it does not exist."""
    if not os.path.exists(db_path):
        create_database_schema(db_path)


# Main CLI function
@click.group()
def cli():
    # Define the path for the SQLite database
    db_path = get_database_path()
    # Initialize database if necessary
    initialize_database(db_path)


# Register click_commands from click_commands directory
cli.add_command(checklist)
cli.add_command(add)
cli.add_command(remove)
cli.add_command(list)
cli.add_command(view)
cli.add_command(create)
cli.add_command(delete)
cli.add_command(edit)
cli.add_command(import_lighterpack)

if __name__ == "__main__":
    cli()
