"""
customer.py - Customer class for the Restaurant Management System.
"""


class Customer:
    """Represents a restaurant customer."""

    def __init__(self, customer_id, name, phone, order_history=None):
        """
        Initialise a Customer.

        Args:
            customer_id (str): Unique identifier for the customer.
            name (str): Full name of the customer.
            phone (str): Contact phone number.
            order_history (list): List of order IDs associated with this customer.
        """
        self.customer_id = customer_id
        self.name = name
        self.phone = phone
        self.order_history = order_history if order_history else []

    def display(self):
        """Print a formatted summary of the customer."""
        print(f"  [{self.customer_id}] {self.name} | Phone: {self.phone} | Orders: {len(self.order_history)}")

    def add_order(self, order_id):
        """
        Add an order ID to the customer's order history.

        Args:
            order_id (str): The order ID to record.
        """
        self.order_history.append(order_id)
        print(f"Order '{order_id}' added to {self.name}'s history.")

    def get_order_history(self):
        """
        Print the customer's full order history.

        Returns:
            list: List of order IDs.
        """
        if not self.order_history:
            print(f"{self.name} has no previous orders.")
        else:
            print(f"Order history for {self.name}:")
            for oid in self.order_history:
                print(f"  - {oid}")
        return self.order_history

    def update_phone(self, new_phone):
        """
        Update the customer's phone number.

        Args:
            new_phone (str): The new phone number.

        Raises:
            ValueError: If the phone number is empty.
        """
        if not new_phone.strip():
            raise ValueError("Phone number cannot be empty.")
        self.phone = new_phone.strip()
        print(f"Phone number for {self.name} updated to {self.phone}.")

    def to_csv_row(self):
        """
        Return customer data as a list suitable for CSV writing.

        Returns:
            list: [customer_id, name, phone, order_history_joined]
        """
        return [self.customer_id, self.name, self.phone, "|".join(self.order_history)]

    def __str__(self):
        return f"{self.name} (ID: {self.customer_id})"
