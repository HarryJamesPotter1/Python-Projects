import math as M
import numpy as np
from datetime import datetime as D
import qrcode as Q

continue2 = "Y"
while continue2 == "Y":
    print("")
    print("Welcome to Calculator")
    print("")
    Oper = str(input("Enter the operation (1 - Addition, 2 - Subtraction, 3 - Multiply, 4 - Division with Remainder, 5 - Divison without Remainder, 6 - Exponent, 7 - Floor Division, 8 - Less Than, 9 - Greater Than, 10 - Equal, 11 - Factorial, 12 - Square Root, 13 - Cube Root, 14 - Rounding Up, 15 - Rounding Down, 16 - Live Clock, 17 - QR Code, 18 - Abs, 19 - D/R, 20 - R/D, 21 - Sin, 22 - Cos, 23 - Tan, 24 - Asin, 25 - Acos, 26 - Atan, 27 - Log10, 28 - Log) : "))
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
            Result = Num1 / Num2
            print("The first number is the quotient and the second number is the remainder")
            print(Num1, ' / ', Num2, ' = ', Result)
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
            Result = M.pow(Num1, Num2)
            print(Num1, ' ** ', Num2, ' = ', Result)
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ")

        elif Oper == "7":
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

        elif Oper == "8":
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
            
        elif Oper == "9":
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

        elif Oper == "10":
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

        elif Oper == "11":
            print("")
            Num1 = float(input("Input a number to compute the factorial (Numbers from 1 to 2147483647 only): "))
            print("")
            print("* = Multiply, / = Division, ** = Exponent, // = Floor Division, ! = Factorial")
            print("")
            Result = M.factorial(Num1)
            print('Result: ')
            print("")
            print(Num1, '!', '=', Result)
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ")

        elif Oper == "12":
            print("")
            Num1 = float(input("What is the number you want to find the square root of? (No Negative numbers): "))
            Result = M.sqrt(Num1)
            print("The square root of", Num1, "is", Result )
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ")

        elif Oper == "13":
            print("")
            Num1 = float(input("What is the number you want to find the cube root of? (No Negative numbers): "))
            Result = np.cbrt(Num1)
            print("The cube root of", Num1, "is", Result)
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ")

        elif Oper == "14":
            print("")
            Num1 = float(input("Enter a number: "))
            Result = M.ceil(Num1)
            print(Num1, "is rounded up to", Result)
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ")

        elif Oper == "15":
            print("")
            Num1 = float(input("Enter a number: "))
            Result = M.floor(Num1)
            print(Num1, "is rounded down to", Result)
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ")                     

        elif Oper == "16":
            Time = D.now()
            print("")
            print(" It is in Year-Month-Date, Hours: Minutes: Seconds: Milliseconds Format")
            print("")
            print("Live Time:", Time)
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ")

        elif Oper == "17":
            print("")
            version= input("How complicated should the picutre be? (Only from 1 to 40): ")
            qr= Q.QRCode(version, box_size= 10, border= 8)
            print("")
            data = input("What do you want to turn into QR Code: ")

            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image(fill="black", back_color = "white")
            print("")
            img.save(input("Name the file and choose the format (Recommend PNG, JPQ or PDF): "))
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ")

        elif Oper == "18":
            Num1 = float(input("Enter a number: "))
            Result = M.fabs(Num1)
            print("")
            print("Result: ", (Result))
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ")        

        elif Oper == "19":
            print("")
            Num1 = float(input("Enter a number: "))
            Result = M.radians(Num1)
            print("")
            print("Result: ", Result)
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ")        

        elif Oper == "20":
            print("")
            Num1 = float(input("Enter a number: "))
            Result = M.degrees(Num1)
            print("")
            print("Result: ", (Result))
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ")        
       
        elif Oper == "21":
            print("")
            Num1 = float(input("Enter a number: "))
            Result = M.sin(Num1)
            print("")
            print("Result: ", (Result))
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ")        

        elif Oper == "22":
            print("")
            Num1 = float(input("Enter a number: "))
            Result = M.cos(Num1)
            print("")
            print("Result: ", (Result))
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ")        

        elif Oper == "23":
            print("")
            Num1 = float(input("Enter a number: "))
            Result = M.tan(Num1)
            print("")
            print("Result: ", (Result))
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ")        

        elif Oper == "24":
            print("")
            Num1 = float(input("Enter a number: "))
            Result = M.asin(Num1)
            print("")
            print("Result: ", (Result))
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ")        

        elif Oper == "25":
            print("")
            Num1 = float(input("Enter a number: "))
            Result = M.acos(Num1)
            print("")
            print("Result: ", (Result))
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ")        

        elif Oper == "26":
            print("")
            Num1 = float(input("Enter a number: "))
            Result = M.atan(Num1)
            print("")
            print("Result: ", (Result))
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ")        

        elif Oper == "27":
            print("")
            Num1 = float(input("Enter a number: "))
            Result = M.log10(Num1)
            print("")
            print("Result: ", (Result))
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ")        

        elif Oper == "28":
            print("")
            Num1 = float(input("Enter a number: "))
            Num2 = float(input("Enter another number: "))
            Result = M.log(Num2, Num1)
            print("")
            print("Result: ", (Result))
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ")              

        else:
            print("Invalid Operation entry, Please try again")
            print("")
       
        if continue3 != "Y":
            print("")
            continue2 = input("Do you want to continue (Y / N)? : ")