# import requests

# # Download a web page
# response = requests.get("https://api.github.com")
# print(response.status_code)  # Should print 200

# def say_goodbye():
#     print("Goodbye!")
#     print("See you later!")

# # Call it multiple times
# say_goodbye()
# say_goodbye()
# say_goodbye()

# Local variables
# def calculate_price():
#     price = 100
#     tax = price * 0.1
#     print(f"Total: {price + tax}")

# calculate_price()  # Total: 110

# # This fails - price doesn't exist outside the function
# print(price)  # NameError: name 'price' is not defined

# Global variables
# discount_rate = 0.15  # Global variable

# def apply_discount(price):
#     discount = price * discount_rate  # Can read global variable
#     return price - discount

# result = apply_discount(100)
# print(result)  # 85.0


# Modifying global variables
# counter = 0  # Global variable

# def increment():
#     global counter  # Declare we want to modify the global variable
#     counter += 1

# increment()
# increment()
# print(counter)  # 2


# Bad - using global variable
# total = 0

# def add_to_total(amount):
#     global total
#     total += amount

# # Good - using parameters and return
# def add_amounts(current_total, amount):
#     return current_total + amount

# total = 0
# total = add_amounts(total, 10)
# total = add_amounts(total, 20)
# print(total)  # 30

# Without parameters (inflexible)
# def greet_alice():
#     print("Hello, Alice!")

# # With parameters (flexible)
# def greet(name):
#     print(f"Hello, {name}!")

# # Now it works for anyone
# greet("Alice")
# greet("Bob")
# greet("Charlie")

# def introduce(name, age):
#     print(f"My name is {name}")
#     print(f"I am {age} years old")

# # Call with values
# introduce("Alice", 25)
# introduce("Bob", 30)

# def calculate_total(price, tax_rate, discount):
#     tax = price * tax_rate
#     final_price = price + tax - discount
#     print(f"Total: ${final_price}")

# # Order matters!
# calculate_total(100, 0.08, 10)  # $98


# def greet(name, greeting="Hello"):
#     print(f"{greeting}, {name}!")

# # Use default
# greet("Alice")           # Hello, Alice!

# # Override default
# greet("Bob", "Hi")       # Hi, Bob!
# greet("Charlie", "Hey")  # Hey, Charlie!


# def create_profile(name, age, city):
#     print(f"{name}, {age}, from {city}")

# # Positional arguments (order matters)
# create_profile("Alice", 25, "NYC")

# # Keyword arguments (order doesn't matter)
# create_profile(city="NYC", age=25, name="Alice")
# create_profile(name="Bob", city="LA", age=30)


# This function only prints
# def add_print(a, b):
#     print(a + b)

# # This function returns a value
# def add_return(a, b):
#     return a + b

# # Now you can use the result
# result = add_return(5, 3)
# print(f"The result is {result}")  # The result is 8

# def calculate_area(width, height):
#     area = width * height
#     return area

# # Store the returned value
# room_area = calculate_area(10, 12)
# print(f"Room size: {room_area} sq ft")  # Room size: 120 sq ft


def double(number):
    return number * 2

# Store in variable
result = double(5)

# Use in expressions
# total = double(5) + double(3)  # 10 + 6 = 16

# # Pass to other functions
# print(double(10))  # 20

# # Use in conditions
# if double(7) > 10:
#     print("Big number!")

# Returning multiple values
# Python can return multiple values as a tuple:

# def get_min_max(numbers):
#     return min(numbers), max(numbers)

# # Get both values
# minimum, maximum = get_min_max([5, 2, 8, 1, 9])
# print(f"Min: {minimum}, Max: {maximum}")  # Min: 1, Max: 9

# # Or as a tuple
# result = get_min_max([5, 2, 8, 1, 9])
# print(result)  # (1, 9)

# packages
# Date and time
import datetime
today = datetime.date.today()
print(today)  # 2024-01-15

# Operating system
import os
current_dir = os.getcwd()
print(current_dir)

# JSON data
import json
data = {"name": "Alice", "age": 30}
json_string = json.dumps(data)
print(json_string)  # {"name": "Alice", "age": 30}