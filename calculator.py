# https://github.com/reeceholtuf/lab11-RH-RR
# Partner 1: Reece Holt
# Partner 2: Rohith Rayudu

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0

def logarithm(a, b):
    try:
        return math.log(b, a)
    except ValueError:
        return 0

def exponent(a, b):
    return a ** b





