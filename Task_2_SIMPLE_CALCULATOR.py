#  SIMPLE CALCULATOR

#Function to perform the calculation
def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by Zero!"
    else:
        return "Invalid Operation"
    
#Main Program
try:
    #Get user input
    num1 = float(input("Enter the first number:"))
    num2 = float(input("Enter the second number:"))
    operation = input("Enter the Operation:")
    
    #Perform Calculation
    result = calculate(num1, num2, operation)
    
    #Display the result
    print("The result is:", result)
    
except ValueError:
    print("Invalid input! Please enter numeric values.")