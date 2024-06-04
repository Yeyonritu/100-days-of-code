#   Functions with Outputs
import arts as art
import os
print(art.logo)

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    
    
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

def calculator():
    num1 = float(input("What's the first number?: "))

    for key in operations:
        print(key)
    
    is_calculating = True
    
    while is_calculating:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        user_decision = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        
        if user_decision == 'y':
            num1 = answer
            
        else:
            cls()
            is_calculating = False
            calculator()

calculator()