# inventory.py

def load_inventory():
    inventory = {}
    with open("inventory.txt", "r") as f:
        for line in f:
            name, price, qty = line.strip().split(",")
            inventory[name] = {
                "price": float(price),
                "quantity": int(qty)
            }
    return inventory


def save_inventory(inventory):
    with open("inventory.txt", "w") as f:
        for name, data in inventory.items():
            f.write(f"{name},{data['price']},{data['quantity']}\n")


def show_inventory():
    inventory = load_inventory()
    print("\n=== INVENTORY ===")
    for name, data in inventory.items():
        print(f"{name} — ${data['price']} — {data['quantity']} in stock")
    print()
