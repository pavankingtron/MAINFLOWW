
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is undefined."
    return a / b
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def get_operation():
    operations = {
        '1': add,
        '2': subtract,
        '3': multiply,
        '4': divide
    }
    while True:
        print("\nSelect an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        
        choice = input("Enter the number of the operation (1/2/3/4): ")
        if choice in operations:
            return operations[choice]
        else:
            print("Invalid choice! Please select a valid operation.")

def calculator():
    print("Welcome to the Command-line Calculator!")
    while True:
       
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")
        
      
        operation = get_operation()
        result = operation(num1, num2)
        
        
        print(f"Result: {result}")

        
        again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Thank you for using the calculator. Goodbye!")
            break


calculator()
