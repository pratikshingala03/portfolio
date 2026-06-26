"""
bill.py - Bill class for the Restaurant Management System.
"""


class Bill:
    """Represents a bill generated for a completed order."""

    def __init__(self, bill_id, order, tax_rate=0.19, discount=0.0, paid=False):
        """
        Initialise a Bill.

        Args:
            bill_id (str): Unique identifier for the bill.
            order (Order): The Order object this bill is based on.
            tax_rate (float): Tax rate as a decimal (default 19% German VAT).
            discount (float): Discount as a decimal (e.g. 0.10 = 10%).
            paid (bool): Whether the bill has been paid.
        """
        self.bill_id = bill_id
        self.order = order
        self.tax_rate = float(tax_rate)
        self.discount = float(discount)
        self.paid = paid if isinstance(paid, bool) else paid == "True"

    def calculate_total(self):
        """
        Calculate the final total including tax and discount.

        Returns:
            float: Final amount due.
        """
        subtotal = self.order.get_total()
        discounted = subtotal * (1 - self.discount)
        total = discounted * (1 + self.tax_rate)
        return round(total, 2)

    def apply_discount(self, discount_rate):
        """
        Apply a discount to the bill.

        Args:
            discount_rate (float): Discount as a decimal between 0 and 1.

        Raises:
            ValueError: If the discount rate is out of range.
        """
        if not (0 <= discount_rate <= 1):
            raise ValueError("Discount rate must be between 0 and 1.")
        self.discount = discount_rate
        print(f"Discount of {discount_rate * 100:.0f}% applied to bill {self.bill_id}.")

    def mark_paid(self):
        """
        Mark the bill as paid.

        Raises:
            RuntimeError: If the bill has already been paid.
        """
        if self.paid:
            raise RuntimeError(f"Bill {self.bill_id} has already been paid.")
        self.paid = True
        print(f"Bill {self.bill_id} marked as paid. Thank you!")

    def print_bill(self):
        """Print a formatted receipt for the bill."""
        subtotal = self.order.get_total()
        discount_amount = subtotal * self.discount
        after_discount = subtotal - discount_amount
        tax_amount = after_discount * self.tax_rate
        total = self.calculate_total()
        status = "PAID" if self.paid else "UNPAID"

        print("\n" + "=" * 40)
        print(f"  BILL ID   : {self.bill_id}")
        print(f"  Order ID  : {self.order.order_id}")
        print(f"  Customer  : {self.order.customer.name}")
        print("-" * 40)
        for item in self.order.items:
            print(f"  {item.name:<25} €{item.price:>6.2f}")
        print("-" * 40)
        print(f"  Subtotal            : €{subtotal:.2f}")
        if self.discount > 0:
            print(f"  Discount ({self.discount * 100:.0f}%)       : -€{discount_amount:.2f}")
        print(f"  VAT ({self.tax_rate * 100:.0f}%)            : +€{tax_amount:.2f}")
        print(f"  TOTAL               : €{total:.2f}")
        print(f"  Status              : {status}")
        print("=" * 40 + "\n")

    def to_csv_row(self):
        """
        Return bill data as a list suitable for CSV writing.

        Returns:
            list: [bill_id, order_id, tax_rate, discount, total, paid]
        """
        return [self.bill_id, self.order.order_id, self.tax_rate,
                self.discount, self.calculate_total(), self.paid]

    def __str__(self):
        return f"Bill {self.bill_id} | Total: €{self.calculate_total():.2f} | {'Paid' if self.paid else 'Unpaid'}"
