#provides an interactive, menu-driven command-line interface for managing
#menu items, customers, orders, and bills.

import data_manager as dm
from menu import MenuItem
from customer import Customer
from order import Order
from bill import Bill

def next_id(collection, prefix):
    if not collection:
        return f"{prefix}001"
    numbers = []
    for key in collection:
        try:
            numbers.append(int(key[len(prefix):]))
        except ValueError:
            pass
    return f"{prefix}{max(numbers) + 1:03d}"

def print_header(title):
    """Print a formatted section header."""
    print("\n" + "=" * 45)
    print(f"  {title}")
    print("=" * 45)


def pause():
    """Wait for the user to press Enter before continuing."""
    input("\nwelcome to our Restaurant.")

def view_menu(menu):
    # shoe all the menu items
    print_header("MENU")
    categories = sorted({item.category for item in menu.values()})
    if not categories:
        print(" The menu is empty.")
        return
    for category in categories:
        print(f"\n --- {category} ---")
        for item in menu.values():
            if item.category == category:
                item.display()


def add_menu_item(menu):
    """Prompt the user to add a new item to the menu."""
    print_header("ADD MENU ITEM")
    try:
        name = input(" Item name     : ").strip()
        if not name:
            raise ValueError("Name cannot be empty.")
        category = input(" Category      : ").strip()
        price = float(input("  Price (€)     : ").strip())
        if price <= 0:
            raise ValueError("Price must be positive.")
        item_id = next_id(menu,"M")
        item = MenuItem(item_id, name, category, price)
        menu[item_id] = item
        dm.save_menu(menu)
        print(f" Item '{name}' added with ID {item_id}.")
    except ValueError as e:
        print(f" [Error] {e}")


def toggle_item_availability(menu):
    """Toggle the availability of a menu item."""
    view_menu(menu)
    item_id = input("\nEnter item ID to toggle: ").strip().upper()
    if item_id not in menu:
        print(" [Error] Item not found.")
        return
    menu[item_id].toggle_availability()
    dm.save_menu(menu)

def view_customers(customers):
    """Display all registered customers."""
    print_header("CUSTOMERS")
    if not customers:
        print(" No customers registered.")
        return
    for customer in customers.values():
        customer.display()

def add_customer(customers):
    """ register a new customer."""
    print_header("ADD CUSTOMER")
    try:
        name = input(" Full name  : ").strip()
        if not name:
            raise ValueError("Name cannot be empty.")
        phone = input(" Phone      : ").strip()
        if not phone:
            raise ValueError("Phone cannot be empty.")
        customer_id = next_id(customers, "C")
        customer = Customer(customer_id, name, phone)
        customers[customer_id] = customer
        dm.save_customers(customers)
        print(f" Customer '{name}' registered with ID {customer_id}.")
    except ValueError as e:
        print(f" [Error] {e}")
def place_order(menu, customers, orders):
    """Place a new order for a customer."""
    print_header("PLACE ORDER")

    if not customers:
        print(" [Error] No customers registered. Please add a customer first.")
        return

    view_customers(customers)
    customer_id = input("\nEnter customer ID: ").strip().upper()
    if customer_id not in customers:
        print(" [Error] Customer not found.")
        return

    customer = customers[customer_id]
    order_id = next_id(orders, "O")
    order = Order(order_id, customer)

    while True:
        view_menu(menu)
        print("\nEnter item ID to add (or 'done' to finish, 'cancel' to abort):")
        choice = input("  > ").strip().upper()

        if choice == "DONE":
            if not order.items:
                print(" [Error] Cannot place an empty order.")
                return
            break
        elif choice == "CANCEL":
            print(" Order cancelled.")
            return
        elif choice in menu:
            try:
                order.add_item(menu[choice])
            except ValueError as e:
                print(f" [Error] {e}")
        else:
            print(" [Error] Item ID not found.")

    orders[order_id] = order
    customer.add_order(order_id)
    dm.save_orders(orders)
    dm.save_customers(customers)
    order.display()
    print(f"\nOrder {order_id} placed successfully!")


def view_orders(orders):
    """Display all orders."""
    print_header("ALL ORDERS")
    if not orders:
        print(" No orders found.")
        return
    for order in orders.values():
        order.display()


def update_order_status(orders):
    """Update the status of an existing order."""
    print_header("UPDATE ORDER STATUS")
    view_orders(orders)
    order_id = input("\nEnter order ID: ").strip().upper()
    if order_id not in orders:
        print(" [Error] Order not found.")
        return

    print(f" Valid statuses: {Order.VALID_STATUSES}")
    new_status = input(" New status    : ").strip()
    try:
        orders[order_id].update_status(new_status)
        dm.save_orders(orders)
    except ValueError as e:
        print(f" [Error] {e}")

def generate_bill(orders, bills):
    """Generate a bill for a served order."""
    print_header("GENERATE BILL")

    billed_order_ids = {bill.order.order_id for bill in bills.values()}
    unbilled = {oid: o for oid, o in orders.items() if oid not in billed_order_ids}

    if not unbilled:
        print(" No unbilled orders available.")
        return

    print(" Unbilled orders:")
    for order in unbilled.values():
        print(f"    [{order.order_id}] {order.customer.name} - €{order.get_total():.2f} [{order.status}]")

    order_id = input("\nEnter order ID to bill: ").strip().upper()
    if order_id not in unbilled:
        print(" [Error] Order not found or already billed.")
        return

    bill_id = next_id(bills, "B")
    bill = Bill(bill_id, orders[order_id])

    discount_input = input(" Apply discount? (e.g. 0.10 for 10%, or 0 for none): ").strip()
    try:
        discount = float(discount_input)
        if discount > 0:
            bill.apply_discount(discount)
    except ValueError:
        print(" [Warning] Invalid discount input. No discount applied.")

    bills[bill_id] = bill
    dm.save_bills(bills)
    bill.print_bill()


def pay_bill(bills):
    """Mark a bill as paid."""
    print_header("PAY BILL")
    unpaid = {bid: b for bid, b in bills.items() if not b.paid}

    if not unpaid:
        print(" No unpaid bills.")
        return

    print(" Unpaid bills:")
    for bill in unpaid.values():
        print(f" [{bill.bill_id}] Order {bill.order.order_id} - €{bill.calculate_total():.2f}")

    bill_id = input("\nEnter bill ID to pay: ").strip().upper()
    if bill_id not in unpaid:
        print(" [Error] Bill not found or already paid.")
        return

    try:
        bills[bill_id].mark_paid()
        dm.save_bills(bills)
    except RuntimeError as e:
        print(f" [Error] {e}")

def main():
    """Run the Restaurant Management System."""
    print("\nLoading data...")
    menu = dm.load_menu()
    menu = dm.seed_menu_if_empty(menu)
    dm.save_menu(menu)

    customers = dm.load_customers()
    orders = {}   # Orders are rebuilt each session from CSV in a full implementation
    bills = {}    # Same note as above

    while True:
        print_header("RESTAURANT MANAGEMENT SYSTEM")
        print("1. View Menu")
        print("2. Add Menu Item")
        print("3. Toggle Item Availability")
        print("  ─────────────────────────────")
        print("4. View Customers")
        print("5. Add Customer")
        print("  ─────────────────────────────")
        print("6. Place Order")
        print("7. View Orders")
        print("8. Update Order Status")
        print("  ─────────────────────────────")
        print("9. Generate Bill")
        print("10. Pay Bill")
        print("  ─────────────────────────────")
        print("0. Exit")

        choice = input("\nSelect an option: ").strip()

        if choice == "1":
            view_menu(menu)
            pause()
        elif choice == "2":
            add_menu_item(menu)
            pause()
        elif choice == "3":
            toggle_item_availability(menu)
            pause()
        elif choice == "4":
            view_customers(customers)
            pause()
        elif choice == "5":
            add_customer(customers)
            pause()
        elif choice == "6":
            place_order(menu, customers, orders)
            pause()
        elif choice == "7":
            view_orders(orders)
            pause()
        elif choice == "8":
            update_order_status(orders)
            pause()
        elif choice == "9":
            generate_bill(orders, bills)
            pause()
        elif choice == "10":
            pay_bill(bills)
            pause()
        elif choice == "0":
            print("\nHave a nice meal!wish you a lovely day! Goodbye!\n")
            dm.save_menu(menu)
            dm.save_customers(customers)
            break
        else:
            print(" [Error] Invalid option. Please try again.")

if __name__ == "__main__":
    main()
