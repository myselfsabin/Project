# order.py

from inventory import load_inventory, save_inventory

def order_item(item_name, amount):
    inventory = load_inventory()

    if item_name not in inventory:
        return "Item not found."

    inventory[item_name]["quantity"] += amount
    save_inventory(inventory)

    return f"Added {amount} to {item_name} stock."
