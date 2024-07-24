import click
import rich
from database import get_item, update_item
from item import print_item_view

option = f'''
[underline]What would you like to edit?[/underline]

 1. Name
 2. Note
 3. Weight
 4. Category

 5. Save and Exit
 6. Cancel
'''


@click.group()
def edit():
    """Update items and collections."""


@edit.command()
@click.argument("item_id", required=True, type=int)
def item(item_id: int):
    item = get_item(item_id)

    #  TODO: fix this codesmell!
    while True:
        print_item_view(item)
        rich.print(option)
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
                    print("Invalid input. Please enter a numeric value for weight.")
        elif choice == '4':
            item.category = input("Enter new category: ")
        elif choice == '5':
            if input("Do you want to save changes? (yes/no]): ").lower() in ('yes', 'y'):
                print("Changes saved.")
                update_item(item)
                return
            else:
                print("Save cancelled.")
        elif choice == '6':
            print("Edit cancelled.")
            return item
        else:
            print("Invalid choice. Please try again.")
