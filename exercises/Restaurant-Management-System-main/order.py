"""
order.py - Order class for the Restaurant Management System.
"""

from datetime import datetime


class Order:
    """Represents a customer order containing one or more menu items."""

    VALID_STATUSES = ["Pending", "In Progress", "Served", "Cancelled"]

    def __init__(self, order_id, customer, items=None, status="Pending", timestamp=None):
        """
        Initialise an Order.

        Args:
            order_id (str): Unique identifier for the order.
            customer (Customer): The Customer object placing the order.
            items (list): List of MenuItem objects in the order.
            status (str): Current status of the order.
            timestamp (str): Time the order was placed (defaults to now).
        """
        self.order_id = order_id
        self.customer = customer
        self.items = items if items else []
        self.status = status
        self.timestamp = timestamp if timestamp else datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def add_item(self, menu_item):
        """
        Add a MenuItem to the order.

        Args:
            menu_item (MenuItem): The item to add.

        Raises:
            ValueError: If the item is not available.
        """
        if not menu_item.available:
            raise ValueError(f"'{menu_item.name}' is currently unavailable.")
        self.items.append(menu_item)
        print(f"Added '{menu_item.name}' to order {self.order_id}.")

    def remove_item(self, item_id):
        """
        Remove a menu item from the order by item ID.

        Args:
            item_id (str): The ID of the item to remove.

        Raises:
            ValueError: If the item is not found in the order.
        """
        for item in self.items:
            if item.item_id == item_id:
                self.items.remove(item)
                print(f"Removed '{item.name}' from order {self.order_id}.")
                return
        raise ValueError(f"Item ID '{item_id}' not found in this order.")

    def get_total(self):
        """
        Calculate and return the subtotal of all items in the order.

        Returns:
            float: Sum of all item prices.
        """
        return sum(item.price for item in self.items)

    def update_status(self, new_status):
        """
        Update the status of the order.

        Args:
            new_status (str): One of the VALID_STATUSES.

        Raises:
            ValueError: If the status is not recognised.
        """
        if new_status not in self.VALID_STATUSES:
            raise ValueError(f"Invalid status. Choose from: {self.VALID_STATUSES}")
        self.status = new_status
        print(f"Order {self.order_id} status updated to '{self.status}'.")

    def display(self):
        """Print a formatted summary of the order."""
        print(f"\n  Order ID : {self.order_id}")
        print(f"  Customer : {self.customer.name}")
        print(f"  Status   : {self.status}")
        print(f"  Time     : {self.timestamp}")
        print(f"  Items    :")
        if self.items:
            for item in self.items:
                print(f"    - {item.name} (€{item.price:.2f})")
        else:
            print("    (no items)")
        print(f"  Subtotal : €{self.get_total():.2f}")

    def to_csv_row(self):
        """
        Return order data as a list suitable for CSV writing.

        Returns:
            list: [order_id, customer_id, item_ids_joined, status, timestamp]
        """
        item_ids = "|".join(item.item_id for item in self.items)
        return [self.order_id, self.customer.customer_id, item_ids, self.status, self.timestamp]

    def __str__(self):
        return f"Order {self.order_id} for {self.customer.name} [{self.status}]"
