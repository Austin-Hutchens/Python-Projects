Easy-to-Alter Italian Restaurant Menu

Overview

This project showcases a simplified, object-oriented system for managing restaurant menus, franchises, and businesses. It was created as part of a learning experience to demonstrate fundamental Python programming skills, particularly in object-oriented design.

Features

Menu Management

Create and manage menus with specific items, prices, and availability times.

Calculate the total bill for purchased items using the calculate_bill method.

Display menu details, including name and availability, with a custom string representation.

Franchise Management

Represent franchises with unique addresses and associated menus.

Determine available menus based on a specific time using the available_menus method.

Business Representation

Organize franchises under a single business entity.

Manage multiple businesses with distinct names and franchise lists.

Demonstrated Skills

This project highlights proficiency in:

Object-Oriented Programming

Classes and Objects:

Menu, Franchise, and Business classes represent key components of the restaurant system.

Constructors (__init__):

Initialize class instances with relevant attributes like name, items, addresses, and menus.

Encapsulation:

Use methods like calculate_bill and available_menus to encapsulate functionality within the respective classes.

String Representation

Custom __str__ Methods:

Provide human-readable representations of Menu and Franchise objects for easy debugging and output.

Iteration and Logic

Menu Item Calculation:

Iterate over purchased items to compute the total cost.

Time-Based Filtering:

Determine available menus by comparing times within specific ranges.

How to Use

Clone the repository to your local machine.

Run the Python script in any Python 3.8+ environment.

Explore the provided examples, such as calculating bills and determining available menus at different times.

Example Output

Menu Representation

Brunch Menu: Available from 11:00 to 16:00

Bill Calculation

The total bill for the brunch order is: $13.00

Available Menus

Menus available at 12:00:
Brunch Menu: Available from 11:00 to 16:00
Kids Menu: Available from 11:00 to 21:00

Project Structure

Menu Class: Represents individual menus with items, prices, and time availability.

Franchise Class: Represents restaurant locations and handles menu availability.

Business Class: Groups franchises under a single business entity.

Purpose

This project serves as a foundation for learning and applying object-oriented programming principles. It demonstrates how to:

Model real-world systems with classes.

Organize and manage data using methods and attributes.

Apply logic to solve practical problems in a structured way.

Feel free to modify and expand this project to suit your needs!



