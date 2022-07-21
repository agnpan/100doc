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
    while continue_calculating[0] not in ("y", "n", "a"):
        continue_calculating = input("""Do you want to add another operation? Type 'yes' or 'no'. 
Type 'again' to clear and start a new operation: """).lower()

    return continue_calculating
    

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    my_calculation = True

    while my_calculation:
        num1 = float(input("What's the first number? "))
        
        operation_symbol = " "
        for symbol in operations:
            print(symbol)
        while operation_symbol not in operations:
            operation_symbol = input("Pick an operator from the line above: ")
        
        num2 = float(input("What's the second number? "))
        
        calculation = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {calculation}")
        
        keep_counting = True
        while keep_counting:
            continue_calculating = continue_calculations()
            
            if continue_calculating[0] == "n":
                keep_counting = False
            elif continue_calculating[0] == "y":
                for symbol in operations: # not working
                    print(symbol)
                operation_symbol = input("Pick an operator from the line above: ")
                new_num = float(input("What is the next number? "))
                
                previous_calculation = calculation
                new_calculation = operations[operation_symbol](calculation, new_num)
                print(f"{previous_calculation} {operation_symbol} {new_num} = {new_calculation}")
                calculation = new_calculation
            elif continue_calculating[0] == "a":
                for i in range(50):
                    print()
                calculator()
        
        my_calculation = False

print(logo)
calculator()
