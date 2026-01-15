# selling.py

from inventory import load_inventory, save_inventory

def sell_item(item_name, amount):
    inventory = load_inventory()

    if item_name not in inventory:
        return "Item not found."

    if inventory[item_name]["quantity"] < amount:
        return "Not enough stock."

    inventory[item_name]["quantity"] -= amount
    save_inventory(inventory)

    return f"Sold {amount} {item_name}(s)."
