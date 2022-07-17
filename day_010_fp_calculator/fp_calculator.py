# CALCULATOR

from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


print(logo)
num1 = float(input("What's the first number? "))
for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operator from the line above: ")
num2 = float(input("What's the second number? "))

calculation = operations[operation_symbol](num1, num2)
print(f"{num1} {operation_symbol} {num2} = {calculation}")
