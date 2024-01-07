
item_names = ['Laptop', 'Headphones', 'Keyboard', 'Mouse']
item_quantities = [10, 20, 15, 30]

while True:
    
    print("1. View Inventory")
    print("2. Add New Item")
    print("3. Remove Item")
    print("4. Update Item Quantity")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    if choice == '1':
        print("viewing item:")
        for i in range(len(item_names)):
            print(f"{item_names[i]}: {item_quantities[i]}")

    elif choice == '2':
        print("Adding item")
        new_item = input("Ente new item: ")
        new_item_quantity = int(input(f"Ente quantity  {new_item}: "))
        item_names.append(new_item)
        item_quantities.append(new_item_quantity)
        print(f"{new_item_quantity} {new_item}(s) added to the inventory.")

    elif choice == '3':
        print("saw remove item")
        remov_item = input("Enter the  remove item: ")
        if remov_item in item_names:
            index = item_names.index(remov_item)
            del item_names[index]
            del item_quantities[index]
            print(f"{remov_item} removed from the inventory.")
        else:
            print("Item not found.")

    elif choice == '4':
        print("update item")
        update_item = input("Enter the item to update quantity: ")
        if update_item in item_names:
            index = item_names.index(update_item)
            new_quantity = int(input(f"Enter the new quantity for {update_item}: "))
            item_quantities[index] = new_quantity
            print(f"Quantity of {update_item} updat to {new_quantity}.")
        else:
            print("Item not found in the inventory.")

    elif choice == '5':
        print("Exiting the program")
        break

    else:
        print("Invalid choice.")
