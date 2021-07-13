# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

# Exponent Function
def power(x, y):
    return x ** y

# This function lowers down the 1st number to be divisible by the 2nd number
def floor_division(x, y):
    return x // y

print("")
print("Select operation:")
print("")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Exponent")
print("6.Floor Division")

while True:
    # Take input from the user
    print("")
    choice = input("Enter choice(1/2/3/4/5/6): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4', '5', '6'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("")
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print("")
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print("")
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print("")
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '5':
            print("")
            print(num1, "**", num2, "=", power(num1, num2))

        elif choice == '6':
            print("")
            print(num1, "//", num2, "=", floor_division(num1, num2))

    else:
        print("Invalid Input")