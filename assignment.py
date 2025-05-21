# create a inventory managemet -use loops to display or updtae list of stock items



# The system allows the user to add, view, update, and remove items from the inventory.
# The inventory is represented as a list of lists, where each inner list contains the item name and its quantity.
# The program will continue to run until the user chooses to exit.
# Inventory Management System

inventory = []

while True:
    print("\n Inventory Management")
    print("1. Add item")
    print("2. View all items")
    print("3. Update item quantity")
    print("4. Remove item")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    # Add item
    if choice == "1":
        item = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        inventory.append([item, quantity])
        print(f"{item} added with quantity {quantity}")
    
    # View all items
    elif choice == "2":
        if not inventory:
            print("Inventory is empty")
        else:
            print("\nCurrent Inventory:")
            print("Item\t\tQuantity")
            print("-----------------------")
            for item in inventory:
                print(f"{item[0]}\t\t{item[1]}")
    
    # Update quantity
    elif choice == "3":
        item_name = input("Enter item name to update: ")
        found = False
        for item in inventory:
            if item[0].lower() == item_name.lower():
                new_quantity = int(input("Enter new quantity: "))
                item[1] = new_quantity
                print(f"{item_name} quantity updated to {new_quantity}")
                found = True
                break
        if not found:
            print("Item not found in inventory")
    
    # Remove item
    elif choice == "4":
        item_name = input("Enter item name to remove: ")
        for i, item in enumerate(inventory):
            if item[0].lower() == item_name.lower():
                inventory.pop(i)
                print(f"{item_name} removed from inventory")
                break
        else:
            print("Item not found in inventory")
    
    # Exit
    elif choice == "5":
        print("Exiting inventory system")
        break
    
    else:
        print("Invalid choice. Please enter 1-5")