import math

def add(a, b): 
    return a + b

def subtract(a, b): 
    return a - b

def multiply(a, b): 
    return a * b

def divide(a, b): 
    if b == 0: 
        return "Error: Division by zero" 
    else: 
        return a / b

def modulus(a, b): 
    return a % b

def power(a, b): 
    return math.pow(a, b)

def square_root(): 
    val = int(input("Enter a number: ")) 
    if val < 0: 
        return "Error: Square root of negative number" 
    else: 
        return math.sqrt(val)

def percentage(mark, total=500): 
    return f"{sum(mark) / total * 100}%"

# Mapping integer choices directly to function names (no quotes around functions)
inputchoice = {
    1: add, 
    2: subtract, 
    3: multiply, 
    4: divide, 
    5: modulus, 
    6: power
}

while True: 
    print("\n 1) add \n 2) subtract \n 3) multiply \n 4) divide \n 5) modulus \n 6) power \n 7) square_root \n 8) percentage \n 9) exit") 
    
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 9: 
        print("Exiting the calculator.") 
        break 

    elif choice in inputchoice: 
        a = int(input("Enter first number: ")) 
        b = int(input("Enter second number: ")) 
        print("Result:", inputchoice[choice](a, b)) 

    elif choice == 7: 
        print("Result:", square_root()) 

    elif choice == 8: 
        mark = [] 
        for i in range(1, 6): 
            marks = int(input(f"Enter marks of subject {i}: ")) 
            mark.append(marks) 
        print("Result:", percentage(mark)) 

    else: 
        print("Invalid choice")
