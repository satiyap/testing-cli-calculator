#!/usr/bin/env python3
"""
Simple CLI Calculator with Addition Feature

This calculator can add two numbers provided by the user.
"""

import sys


def add_numbers(a, b):
    """Add two numbers and return the result."""
    return a + b


def get_number_input(prompt):
    """Get a number from user input with error handling."""
    while True:
        try:
            value = input(prompt)
            return float(value)
        except ValueError:
            print("Error: Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            sys.exit(0)


def main():
    """Main function to run the calculator."""
    print("Simple Calculator - Addition")
    print("=" * 30)
    
    # Get two numbers from user
    num1 = get_number_input("Enter the first number: ")
    num2 = get_number_input("Enter the second number: ")
    
    # Calculate result
    result = add_numbers(num1, num2)
    
    # Display result
    print(f"\nResult: {num1} + {num2} = {result}")


if __name__ == "__main__":
    main()