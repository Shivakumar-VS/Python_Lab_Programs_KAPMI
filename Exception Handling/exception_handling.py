# 3. Write a Python Program to Demonstrate Exception Handling 
try: 
    x = int(input("Enter the first number: ")) 
    y = int(input("Enter the second number: ")) 
    result = x / y  # Use the division operator 
    print("The result is:", result) 
except ValueError: 
    print("Invalid input, please enter valid numbers!") 
except ZeroDivisionError: 
    print("Error: Cannot divide by zero!")