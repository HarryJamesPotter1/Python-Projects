import math
import numpy as np
from tkinter import Label, Tk 
import time

continue2 = "Y"
while continue2 == "Y":
    print("")
    Oper = str(input("Enter the operation (1 - Addition, 2 - Subtraction, 3 - Multiply, 4 - Division, 5 - Exponent, 6 - Floor Division, 7 - Less Than, 8 - Greater Than, 9 - Equal, 10 - Factorial, 11 - Square Root, 12 - Cube Root, 13 - Rounding Up, 14 - Rounding Down) : "))
    Operation = 0
    continue3 = "Y"
    while continue3 == "Y":

        if Oper == "1":
            print("")
            Num1 = float(input("Enter a number: "))
            Num2 = float(input("Enter another number: "))
            print("")
            print("* = Multiply, / = Division, ** = Exponent, // = Floor Division, ! = Factorial")
            print("")
            print("Result: ")
            print("")
            Result = Num1 + Num2
            print(Num1, ' + ', Num2, ' = ', Result)
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ")                
    
        elif Oper == "2":
            print("")
            Num1 = float(input("Enter a number: "))
            Num2 = float(input("Enter another number: "))
            print("")
            print("* = Multiply, / = Division, ** = Exponent, // = Floor Division, ! = Factorial")
            print("")
            print("Result: ")
            print("")
            Result = Num1 - Num2
            print(Num1, ' - ', Num2, ' = ', Result)
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ")
    
        elif Oper == "3":
            print("")
            Num1 = float(input("Enter a number: "))
            Num2 = float(input("Enter another number: "))
            print("")
            print("* = Multiply, / = Division, ** = Exponent, // = Floor Division, ! = Factorial")
            print("")
            print("Product: ")
            print("")
            Result = Num1 * Num2
            print(Num1, ' * ', Num2, ' = ', Result)
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ")

        elif Oper == "4":
            print("")
            Num1 = float(input("Enter a number: "))
            Num2 = float(input("Enter another number: "))
            print("")
            print("* = Multiply, / = Division, ** = Exponent, // = Floor Division, ! = Factorial")
            print("")
            print("Result: ")
            print("")
            Result = divmod(Num1, Num2)
            print("The first number is the quotient and the second number is the remainder")
            print(Num1, ' / ', Num2, ' = ', Result)
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ")
        
        elif Oper == "5":
            print("")
            Num1 = float(input("Enter a number: "))
            Num2 = float(input("Enter another number: "))
            print("")
            print("* = Multiply, / = Division, ** = Exponent, // = Floor Division, ! = Factorial")
            print("")
            print("Result: ")
            print("")
            Result = math.pow(Num1, Num2)
            print(Num1, ' ** ', Num2, ' = ', Result)
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ")

        elif Oper == "6":
            print("")
            Num1 = float(input("Enter a number: "))
            Num2 = float(input("Enter another number: "))
            print("")
            print("* = Multiply, / = Division, ** = Exponent, // = Floor Division, ! = Factorial")
            print("")
            print("Result: ")
            print("")
            Result = Num1 // Num2
            print(Num1, ' // ', Num2, ' = ', Result)
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ")

        elif Oper == "7":
            print("")
            Num1 = float(input("Enter a number: "))
            Num2 = float(input("Enter another number: "))
            print("")
            print("* = Multiply, / = Division, ** = Exponent, // = Floor Division, ! = Factorial")
            print("")
            if Num1 < Num2:
                print(Num1, ' < ', Num2, ' = ', "True")
                print("")
                continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ")

            else:
                print(Num1, ' < ', Num2, ' = ', "False")
                print("")
                continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ")
            
        elif Oper == "8":
            print("")
            Num1 = float(input("Enter a number: "))
            Num2 = float(input("Enter another number: "))
            print("")
            print("* = Multiply, / = Division, ** = Exponent, // = Floor Division, ! = Factorial")
            print("")
            if Num1 > Num2:
                print(Num1, ' > ', Num2, ' = ', "True")
                print("")
                continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ")

            else:
                print(Num1, ' > ', Num2, ' = ', "False")
                print("")
                continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ")

        elif Oper == "9":
            print("")
            Num1 = float(input("Enter a number: "))
            Num2 = float(input("Enter another number: "))
            print("")
            print("* = Multiply, / = Division, ** = Exponent, // = Floor Division, ! = Factorial")
            print("")
            if Num1 == Num2:
                print(Num1, ' is equal to ', Num2)
                print("")
                continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ")

            else:
                print(Num1, ' is not equal to ', Num2)
                print("")
                continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ")

        elif Oper == "10":
            print("")
            Num1 = int(input("Input a number to compute the factorial (Numbers from 1 to 2147483647 only): "))
            print("")
            print("* = Multiply, / = Division, ** = Exponent, // = Floor Division, ! = Factorial")
            print("")
            Result = math.factorial(Num1)
            print('Result: ')
            print("")
            print(Num1, '!', '=', Result)
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ")

        elif Oper == "11":
            print("")
            Num1 = float(input("What is the number you want to find the square root of? (No Negative numbers): "))
            Result = math.sqrt(Num1)
            print("The square root of", Num1, "is", Result )
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ")

        elif Oper == "12":
            print("")
            Num1 = float(input("What is the number you want to find the cube root of? (No Negative numbers): "))
            Result = np.cbrt(Num1)
            print("The cube root of", Num1, "is", Result)
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ")

        elif Oper == "13":
            print("")
            Num1 = float(input("Enter a number: "))
            Result = math.ceil(Num1)
            print(Num1, "is rounded up to", Result)
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ")

        elif Oper == "14":
            print("")
            Num1 = float(input("Enter a number: "))
            Result = math.floor(Num1)
            print(Num1, "is rounded down to", Result)
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ")                     

        else:
            print("Invalid Operation entry, Please try again")
            print("")
        
        if continue3 != "Y":
            print("")
            continue2 = input("Do you want to continue (Y / N)? : ")

# Time Clock
