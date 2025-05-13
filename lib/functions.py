#!/usr/bin/env python3

# 1. No arguments
def greet_programmer():
    print("Hello, programmer!")

# 2. One required argument
def greet(name):
    print(f"Hello, {name}!")

# 3. Default argument
def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

# 4. Return sum of two numbers
def add(num1, num2):
    return num1 + num2

# 5. Return number halved
def halve(number):
    return number / 2