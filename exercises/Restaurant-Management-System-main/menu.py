"""
menu.py - MenuItem class for the Restaurant Management System.
"""


class MenuItem:
    """Represents a single item on the restaurant menu."""

    def __init__(self, item_id, name, category, price, available=True):
        """
        Initialise a MenuItem.

        Args:
            item_id (str): Unique identifier for the item.
            name (str): Name of the menu item.
            category (str): Category (e.g. 'Starter', 'Main', 'Dessert', 'Drink').
            price (float): Price of the item.
            available (bool): Whether the item is currently available.
        """
        self.item_id = item_id
        self.name = name
        self.category = category
        self.price = float(price)
        self.available = available if isinstance(available, bool) else available == "True"

    def display(self):
        """Print a formatted summary of the menu item."""
        status = "Available" if self.available else "Unavailable"
        print(f"  [{self.item_id}] {self.name} ({self.category}) - €{self.price:.2f} [{status}]")

    def update_price(self, new_price):
        """
        Update the price of the menu item.

        Args:
            new_price (float): The new price to set.

        Raises:
            ValueError: If new_price is not a positive number.
        """
        if new_price <= 0:
            raise ValueError("Price must be a positive number.")
        self.price = float(new_price)
        print(f"Price for '{self.name}' updated to €{self.price:.2f}.")

    def toggle_availability(self):
        """Toggle the availability of the menu item on or off."""
        self.available = not self.available
        status = "available" if self.available else "unavailable"
        print(f"'{self.name}' is now {status}.")

    def to_csv_row(self):
        """
        Return the item data as a list suitable for CSV writing.

        Returns:
            list: [item_id, name, category, price, available]
        """
        return [self.item_id, self.name, self.category, self.price, self.available]

    def __str__(self):
        return f"{self.name} (€{self.price:.2f})"


# --- ADDING ITEMS BELOW ---

# 1. Create the items using: MenuItem(ID, Name, Category, Price)
# Updated list with the fix and new items
# Burgers
item1 = MenuItem("B01", "Hamburger", "Burgers", 7.05)
item2 = MenuItem("B02", "Cheeseburger", "Burgers", 8.30)
item3 = MenuItem("B03", "Meisterburger", "Burgers", 10.30)
item4 = MenuItem("B04", "Hausmeister", "Burgers", 10.30)
item5 = MenuItem("B05", "Chili-Cheeseburger", "Burgers", 8.75)
item6 = MenuItem("B06", "Waldmeister (Veggie)", "Burgers", 9.10)
item7 = MenuItem("B07", "Meister aller Klassen", "Burgers", 12.90)

# Sides
item8 = MenuItem("S01", "Fries", "Sides", 3.90)
item9 = MenuItem("S02", "Cheese Fries", "Sides", 4.90)
item10 = MenuItem("S03", "Chili-Cheese Fries", "Sides", 5.90)

# Dessert
item11 = MenuItem("D01", "Doublechocolate cookie", "Dessert", 3.50)
item12 = MenuItem("D02", "Doublechocolate Shake", "Dessert", 3.90)
item13 = MenuItem("D03", "Vanilla Shake", "Dessert", 3.90)

# Drinks
item14 = MenuItem("T01", "Grevensteiner Beer", "Drinks", 4.50)
item15 = MenuItem("T02", "Coca-Cola", "Drinks", 4.10)
item16 = MenuItem("T03", "Fanta", "Drinks", 4.10)
item17 = MenuItem("T04", "Veltins Beer", "Drinks", 4.50)

# 2. Put them in a list to manage them easily
menu_list = [item1, item2, item3, item4, item5, item6, item7, 
    item8, item9, item10, item11, item12, item13, 
    item14, item15, item16, item17]

# 3. Quick test: Display the menu
print("--- CURRENT MENU ---")
for item in menu_list:
    item.display()