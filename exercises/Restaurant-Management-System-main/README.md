Restaurant Management System – Project Report
1. Introduction

For this project, I chose a restaurant system because it is something we see in real life almost every day. In many small restaurants, tasks like managing menu items, taking orders, handling customers, and preparing bills are still done manually. From what I observed, this can sometimes cause delays, confusion, or even small mistakes in orders and billing.

The main aim of this project was to create a simple command-line based Restaurant Management System that can make these tasks easier and more organized. Instead of writing everything on paper, the system allows staff to handle menu items, customer details, orders, and billing digitally.

The system mainly focuses on:

Managing menu items and checking their availability
Adding and viewing customer details
Placing and managing orders
Generating and completing bills

I tried to keep the system simple so that it can be easily used in a small restaurant without needing advanced technical knowledge.

2. System Design

While designing the system, I used a modular and object-oriented approach. This means the program is divided into different parts, and each part has its own responsibility. This made the project easier to manage and understand during development.

Main Classes
MenuItem
This class stores details of each item, such as its name, category, price, and availability.
Customer
This class is used to store basic customer information like ID, name, and phone number.
Order
This represents an order placed by a customer. It can include multiple menu items and also keeps track of whether the order is pending or completed.
Bill
This class handles billing. It calculates the total amount for an order and checks whether the payment has been made.
Relationships
One customer can place multiple orders
Each order can contain several menu items
Each order has one related bill
Data Management

For storing data, I used:

Dictionaries for temporary storage while the program is running
File handling (using data_manager.py) to save and load data

To keep everything organized, unique IDs are generated using a helper function (next_id). These IDs follow a pattern like:

M001, M002 for menu items
C001, C002 for customers
O001, O002 for orders
B001, B002 for bills

3. Implementation Overview

This project is implemented using basic Python concepts that I learned during my course.

Functions

Each feature, such as adding a customer or placing an order, is written as a separate function. This makes the code easier to read and reuse.

Classes and Objects

I used object-oriented programming to represent real-world things like customers and orders. This helped me organize the code better and keep related data together.

Exception Handling

I used try-except blocks in several places to handle invalid input. For example, if a user enters the wrong ID or incorrect value, the program shows an error message instead of crashing.

Modularity

The code is divided into different files:

menu.py
customer.py
order.py
bill.py
data_manager.py

Each file handles a specific part of the system, which made development more structured.

Readability

While coding, I tried to keep things simple by:

Using clear function names like add_customer and place_order
Keeping the menu interface easy to follow
Writing basic logic instead of overcomplicating things

4. Testing and Demonstration

To check if the system works properly, I tested it with different types of inputs and situations.

Example Scenarios

Placing an Order:

The user selects the option to place an order
Enters the customer ID
Adds items using their item IDs
Confirms the order

Generating a Bill:

The user selects an order that is not billed yet
Can apply a discount if needed
The system calculates the total and displays the bill
Error Handling Examples
If an invalid item ID is entered
→ [Error] Item ID not found.
If the user tries to place an empty order
→ [Error] Cannot place an empty order.
If discount input is incorrect
→ A warning is shown and the system continues
Testing Method

I tested the system manually by trying different cases, including:

No data available
Invalid IDs
Wrong numeric inputs

This helped me identify and fix small issues.

5. Reflection
Challenges Faced

While working on this project, I faced some difficulties:

Understanding how to properly connect classes like Order, Customer, and Bill
Saving data using file handling
Validating user input without making the code too complicated
Lessons Learned

From this project, I learned:

How modular programming makes code easier to manage
How object-oriented programming works in real applications
How to handle user errors and unexpected inputs
Future Improvements

If I continue working on this project, I would like to:

Use a database like SQLite instead of file handling
Create a graphical user interface (GUI)
Build a web version of the system
Add login functionality for admin and staff
Improve how data is stored and managed
Conclusion

This project shows a basic but functional Restaurant Management System built using Python. It helped me apply important concepts like object-oriented programming, modular design, and error handling in a practical way. Overall, it was a useful experience in building a real-world application.
