menu = {
    "Coffee":80,
    "Tea":50,
    "Sandwich":100,
    "Cake":200,
    "Juice":80
}

order = []

def show_menu():
    print("Welcome to Dhruvu's Cafee....")
    print("===== Cafe Menu =====")
    for item, price in menu.items():

        print(f"{item}: ₹{price}")

def take_order():
    item = input("Enter item name to order: ").title()
    if item in menu:
        order.append(item)
        print(f"{item} added to your order.")
    else:
        print("Sorry, we don't have that item.")


def view_bill():
    if not order:
        print("You haven't ordered anything yet.")
    else:
        print("--- Your Order ---")
        total = 0
        for item in order:
            print(f"{item}: ₹{menu[item]}")
            total += menu[item]
        print(f"Total Bill: ₹{total}")


while True:
    print("=== Cafe Management System ===")
    print("1. Show Menu")
    print("2. Order Item")
    print("3. View Bill")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        show_menu()
    elif choice == "2":
        take_order()
    elif choice == "3":
        view_bill()
    elif choice == "4":
        print("Thank you for visiting the cafe....")
        break
    else:
        print("Invalid choice. Please try again.")
