# main.py

from inventory import show_inventory
from selling import sell_item
from order import order_item

def main():
    while True:
        print("==== MAIN MENU ====")
        print("1. Show inventory")
        print("2. Sell item")
        print("3. Order item")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_inventory()

        elif choice == "2":
            item = input("Item name to sell: ").lower()
            try:
                amount = int(input("Amount: "))
            except:
                print("Invalid number.\n")
                continue

            print(sell_item(item, amount))
            print()

        elif choice == "3":
            item = input("Item name to order: ").lower()
            try:
                amount = int(input("Amount: "))
            except:
                print("Invalid number.\n")
                continue

            print(order_item(item, amount))
            print()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()
