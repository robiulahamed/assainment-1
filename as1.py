
item_names = ['Laptop', 'Headphones', 'Keyboard', 'Mouse']
item_quantities = [10, 20, 15, 30]

while True:
    print("1. Display Inventory")
    print("2. View Item Details")
    print("3. Exit")

    CH = input("Enter choice (1, 2, or 3): ")

    if CH == '1':
        print("\nCurrent Inventory:")
        for i in range(len(item_names)):
            print(f"{item_names[i]}: {item_quantities[i]}")

    else if CH == '2':
        item_name = input("Enter the item name to view details: ")
        if item_name in item_names:
            index = item_names.index(item_name)
            print(f"\nItem: {item_name}")
            print(f"Quantity available: {item_quantities[index]}")
        else:
            print("Item not found in the inventory.")

    else if CH == '3':
        print("Exiting the progra")
        break

    else:
        print("Invalid choic enter.")
