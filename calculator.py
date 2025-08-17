#!/usr/bin/env python3
"""
CLI Calculator with basic arithmetic operations
"""

import argparse
import sys

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract second number from first"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide first number by second"""
    # Intentional error: No division by zero check
    return a / b

def main():
    parser = argparse.ArgumentParser(description='CLI Calculator')
    parser.add_argument('operation', choices=['add', 'subtract', 'multiply', 'divide'],
                        help='The operation to perform')
    parser.add_argument('num1', help='First number')
    parser.add_argument('num2', help='Second number')
    
    args = parser.parse_args()
    
    # Intentional error: Not properly handling non-numeric inputs
    a = float(args.num1)
    b = float(args.num2)
    
    # Intentional error: Using string comparison instead of proper operation mapping
    if args.operation == 'add':
        result = add(a, b)
    elif args.operation == 'subtract':
        result = subtract(a, b)
    elif args.operation == 'multiply':
        result = multiply(a, b)
    elif args.operation == 'divide':
        result = divide(a, b)
    
    # Intentional error: Not handling the case where operation might not match
    print(f"Result: {result}")

if __name__ == '__main__':
    main()