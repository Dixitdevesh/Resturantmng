import csv
import datetime

SHOP_NAME = "Dixit's Restaurant"
OWNER_NAME = "Mr. Pavan Kumar Dixit"
ITEMS_FILE = 'items.csv'

def add_item():
    item_id = input("Enter item ID: ")
    name = input("Enter item name: ")
    category = input("Enter item category (Sweets/Veg Food): ")
    quantity = int(input("Enter item quantity: "))
    price = float(input("Enter item price: "))
    
    with open(ITEMS_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([item_id, name, category, quantity, price])
    print(f"Item '{name}' added successfully.")

def view_items():
    try:
        with open(ITEMS_FILE, mode='r') as file:
            reader = csv.DictReader(file)
            print("\n{:<10} {:<30} {:<15} {:<10} {:<10}".format('ID', 'Name', 'Category', 'Quantity', 'Price'))
            print("=" * 75)
            for row in reader:
                print("{:<10} {:<30} {:<15} {:<10} ${:<10.2f}".format(
                    row['ID'], row['Name'], row['Category'],
                    row['Quantity'], float(row['Price'])
                ))
            print("=" * 75)
    except FileNotFoundError:
        print("Items file not found. Please add items directly in the CSV file.")

def update_item():
    item_id = input("Enter item ID to update: ")
    found = False

    try:
        with open(ITEMS_FILE, mode='r') as file:
            reader = list(csv.DictReader(file))
        
        for row in reader:
            if row['ID'] == item_id:
                found = True
                row['Name'] = input(f"Enter new name (current: {row['Name']}): ") or row['Name']
                row['Category'] = input(f"Enter new category (current: {row['Category']}): ") or row['Category']
                row['Quantity'] = input(f"Enter new quantity (current: {row['Quantity']}): ") or row['Quantity']
                row['Price'] = input(f"Enter new price (current: {row['Price']}): ") or row['Price']
        
        if found:
            with open(ITEMS_FILE, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=reader[0].keys())
                writer.writeheader()
                writer.writerows(reader)
            print("Item updated successfully.")
        else:
            print("Item not found.")
    except FileNotFoundError:
        print("Items file not found. Please add items directly in the CSV file.")

def delete_item():
    item_id = input("Enter item ID to delete: ")
    found = False

    try:
        with open(ITEMS_FILE, mode='r') as file:
            reader = list(csv.DictReader(file))

        for row in reader:
            if row['ID'] == item_id:
                found = True
                reader.remove(row)
                print("Item deleted successfully.")
        
        if found:
            with open(ITEMS_FILE, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=reader[0].keys())
                writer.writeheader()
                writer.writerows(reader)
        else:
            print("Item not found.")
    except FileNotFoundError:
        print("Items file not found. Please add items directly in the CSV file.")

def record_sale():
    item_id = input("Enter item ID to sell: ")
    quantity = int(input("Enter quantity to sell: "))
    found = False

    try:
        with open(ITEMS_FILE, mode='r') as file:
            reader = list(csv.DictReader(file))
        
        for row in reader:
            if row['ID'] == item_id:
                found = True
                if int(row['Quantity']) >= quantity:
                    row['Quantity'] = int(row['Quantity']) - quantity
                    total_price = quantity * float(row['Price'])
                    print(f"Sold {quantity} of '{row['Name']}'. Total price: ${total_price:.2f}")
                else:
                    print("Not enough quantity available.")

        if found:
            with open(ITEMS_FILE, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=reader[0].keys())
                writer.writeheader()
                writer.writerows(reader)
        else:
            print("Item not found.")
    except FileNotFoundError:
        print("Items file not found. Please add items directly in the CSV file.")

def main():
    while True:
        print("\nWelcome to", SHOP_NAME)
        print("Owner:", OWNER_NAME)
        print("1. Add Item")
        print("2. View Items")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Record Sale")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_item()
        elif choice == '2':
            view_items()
        elif choice == '3':
            update_item()
        elif choice == '4':
            delete_item()
        elif choice == '5':
            record_sale()
        elif choice == '6':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
