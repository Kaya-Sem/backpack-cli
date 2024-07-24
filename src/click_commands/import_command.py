import click
import csv
import os
from typing import List
from database import create_collection, create_item, add_items_to_collection


@click.command()
@click.argument('input_file', type=click.Path(exists=True, readable=True))
def import_lighterpack(input_file):
    """
    Command to import items from a CSV file into the database and create a collection named after the file.
    """
    import_csv(input_file)


def parse_weight(weight_str: str) -> int:
    """
    Parse the weight string and convert it to grams if necessary.
    """
    if 'kilogram' in weight_str.lower():
        weight_str = weight_str.lower().replace('kilogram', '').strip()
        return int(float(weight_str) * 1000)
    elif 'gram' in weight_str.lower():
        weight_str = weight_str.lower().replace('gram', '').strip()
        return int(weight_str)
    return int(weight_str)


def parse_csv(file_path: str) -> List[dict]:
    """
    Parse the CSV file and return a list of items.
    """
    items = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            weight = parse_weight(row['weight'])
            item = {
                'name': row['Item Name'],
                'weight': weight,
                'category': row['Category'],
                'note': row['desc']  # Use the description as a note
            }
            items.append(item)
    return items


def import_csv(file_path: str):
    # Get the file name without extension
    file_name = os.path.splitext(os.path.basename(file_path))[0]

    # Parse the CSV file
    items = parse_csv(file_path)

    # Create a new collection named after the file name
    collection_id = create_collection(file_name, f"Items imported from {file_name} (lighterpack)")

    # Create items and add them to the collection
    item_ids = []
    for item in items:
        item_id = create_item(item['name'], item['weight'], item['category'], item['note'])
        item_ids.append(item_id)

    add_items_to_collection(collection_id, item_ids)
    print(f"\nImported {len(items)} items from {file_name} and added them to collection {collection_id}.")


if __name__ == "__main__":
    import_lighterpack()
