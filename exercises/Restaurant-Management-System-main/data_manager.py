import csv
import os
from menu import MenuItem

def load_menu(filename="menu_data.csv"):
    """Loads menu items from a CSV file into a dictionary for main.py."""
    menu = {}
    if not os.path.exists(filename):
        return {}
    
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and len(row) >= 4:
                    item_id, name, category, price = row[0], row[1], row[2], row[3]
                    # Handle availability if it exists in the CSV (default to True)
                    available = row[4] == "True" if len(row) > 4 else True
                    menu[item_id] = MenuItem(item_id, name, category, float(price), available)
    except Exception as e:
        print(f"  [Error loading menu] {e}")
    return menu

def save_menu(menu, filename="menu_data.csv"):
    """Saves the menu dictionary back to the CSV file."""
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for item in menu.values():
                writer.writerow(item.to_csv_row())
    except Exception as e:
        print(f"  [Error saving menu] {e}")

def seed_menu_if_empty(menu):
    """
    REQUIRED BY MAIN.PY: 
    Populates the menu with the full Burgermeister list if empty.
    """
    if not menu:
        print("  Menu is empty. Seeding Burgermeister items...")
        items = [
            # Burgers
            MenuItem("B01", "Hamburger", "Burgers", 7.05),
            MenuItem("B02", "Cheeseburger", "Burgers", 8.30),
            MenuItem("B03", "Meisterburger", "Burgers", 10.30),
            MenuItem("B04", "Hausmeister", "Burgers", 10.30),
            MenuItem("B05", "Chili-Cheeseburger", "Burgers", 8.75),
            MenuItem("B06", "Waldmeister (Veggie)", "Burgers", 9.10),
            MenuItem("B07", "Meister aller Klassen", "Burgers", 12.90),
            # Sides
            MenuItem("S01", "Fries", "Sides", 3.90),
            MenuItem("S02", "Cheese Fries", "Sides", 4.90),
            MenuItem("S03", "Chili-Cheese Fries", "Sides", 5.90),
            # Desserts
            MenuItem("D01", "Doublechocolate cookie", "Dessert", 3.50),
            MenuItem("D02", "Doublechocolate Shake", "Dessert", 3.90),
            MenuItem("D03", "Vanilla Shake", "Dessert", 3.90),
            # Drinks
            MenuItem("T01", "Grevensteiner Beer", "Drinks", 4.50),
            MenuItem("T02", "Coca-Cola", "Drinks", 4.10),
            MenuItem("T03", "Fanta", "Drinks", 4.10),
            MenuItem("T04", "Veltins Beer", "Drinks", 4.50)
        ]
        for item in items:
            menu[item.item_id] = item
    return menu

def load_customers(filename="customers.csv"):
    """REQUIRED BY MAIN.PY: Returns an empty dictionary to start."""
    return {}

def save_customers(customers, filename="customers.csv"):
    """REQUIRED BY MAIN.PY: Placeholder for customer saving."""
    pass

def save_orders(orders):
    """REQUIRED BY MAIN.PY: Placeholder for order saving."""
    pass

def save_bills(bills):
    """REQUIRED BY MAIN.PY: Placeholder for bill saving."""
    pass