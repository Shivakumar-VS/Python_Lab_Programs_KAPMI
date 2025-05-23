# 1. Write a Python Program to create a calculator program. 
def calculate(n1, n2, op): 
 if op == '+': 
    result = n1 + n2 
 elif op == '-': 
    result = n1 - n2 
 elif op == '*': 
    result = n1 * n2 
 elif op == '/': 
    if n2 == 0: 
        return "Error: Division by zero!" 
    result = n1 / n2 
 elif op == '**': # Exponentiation operator 
    result = n1 ** n2 
 else: 
    return "Invalid operator!" 
 return result 
# Taking user input 
number1 = float(input("Enter the first number: ")) 
op = input("Enter the operator (+, -, *, /, **): ") 
number2 = float(input("Enter the second number: "))
# Displaying input values 
print(number1, op, number2) 
# Calculating and displaying the result 
result = calculate(number1, number2, op) 
print("=", result) 