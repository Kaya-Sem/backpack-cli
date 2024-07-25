import click
import rich
from database import get_item, update_item, get_collection, update_collection
from item import print_item_view
from collection import print_collection


item_options = f'''
[underline]What would you like to edit?[/underline]

 1. Name
 2. Note
 3. Weight
 4. Category

 s Save and Exit
 c Cancel
'''

collection_options = f'''
[underline]What would you like to edit?[/underline]

 1. Name
 2. Description

 s Save and Exit
 c Cancel
'''


@click.group()
def edit():
    """Update items and collections."""


@edit.command()
@click.argument("collection_id", required=True, type=int)
def collection(collection_id: int):
    collection = get_collection(collection_id)

    while True:
        print_collection(collection)
        rich.print(collection_options)
        choice = click.prompt("Enter your choice")

        if choice == "1":
            collection.name = input("Enter new name: ")
        elif choice == "2":
            collection.description = input("Enter new description: ")
        elif choice == "s":
            update_collection(collection)
            return
        elif choice == "c":
            print("Edit cancelled.")
            return
        else:
            print("Invalid choice. Please try again.")


@edit.command()
@click.argument("item_id", required=True, type=int)
def item(item_id: int):
    item = get_item(item_id)

    #  TODO: fix this codesmell!
    while True:
        print_item_view(item)
        rich.print(item_options)
        choice = click.prompt("Enter your choice")

        if choice == '1':
            item.name = input("Enter new name: ")
        elif choice == '2':
            item.note = input("Enter new note: ")
        elif choice == '3':
            while True:
                try:
                    item.weight = float(input("Enter new weight (g): "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
        elif choice == '4':
            item.category = input("Enter new category: ")
        elif choice == 's':
            if input("Do you want to save changes? (y/n]): ").lower() in ('yes', 'y'):
                update_item(item)
                return
            else:
                print("Save cancelled.")
        elif choice == 'c':
            print("Edit cancelled.")
            return item
        else:
            print("Invalid choice. Please try again.")
