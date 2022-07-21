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


def continue_calculations():
    continue_calculating = " "
    while continue_calculating[0] not in ("y", "n"):
        continue_calculating = input("Do you want to add another operation? Type 'yes' or 'no': ").lower()

    return continue_calculating
    
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


print(logo)

my_calculation = True

while my_calculation:
    num1 = float(input("What's the first number? "))
    
    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick an operator from the line above: ")
    
    num2 = float(input("What's the second number? "))
    
    calculation = operations[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {calculation}")  
       
    keep_counting = True
    
    while keep_counting:
        continue_calculating = continue_calculations()
        if continue_calculating[0] == "n":
            keep_counting = False # working
        elif continue_calculating[0] == "y":
            for symbol in operations: # not working
                print(symbol)
            operation_symbol = input("Pick an operator from the line above: ")
            new_num = float(input("What is the next number? "))
            new_calculation = operations[operation_symbol](calculation, new_num)
            print(f"{calculation} {operation_symbol} {new_num} = {new_calculation}")
            continue

    my_calculation = False
