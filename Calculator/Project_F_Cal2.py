continue2 = "Y"
while continue2 == "Y":
    print("")
    Oper = str(input("Enter the operation (1 - Addition, 2 - Subtraction, 3 - Multiply, 4 - Division, 5 - Exponent, 6 - Floor Division, 7 - Less Than, 8 - Greater Than, 9 - Equal, 10 - Factorial) : "))
    Operation = 0

    if Oper == "1":
        print("")
        Num1 = float(input("Enter a number: "))
        Num2 = float(input("Enter another number: "))
        Num3 = float(input("Enter another number: "))
        print("")
        print("* = Multiply, / = Division, ** = Exponent, // = Floor Division, ! = Factorial")
        print("")
        print("Result: ")
        print("")
        Result = Num1 + Num2
        print(Num1, ' + ', Num2, ' = ', Result)
 
    elif Oper == "2":
        print("")
        Num1 = float(input("Enter a number: "))
        Num2 = float(input("Enter another number: "))
        Num3 = float(input("Enter another number: "))
        print("")
        print("* = Multiply, / = Division, ** = Exponent, // = Floor Division, ! = Factorial")
        print("")
        print("Result: ")
        print("")
        Result = Num1 - Num2
        print(Num1, ' - ', Num2, ' = ', Result)
 
    elif Oper == "3":
        print("")
        Num1 = float(input("Enter a number: "))
        Num2 = float(input("Enter another number: "))
        Num3 = float(input("Enter another number: "))
        print("")
        print("* = Multiply, / = Division, ** = Exponent, // = Floor Division, ! = Factorial")
        print("")
        print("Product: ")
        print("")
        Result = Num1 * Num2
        print(Num1, ' * ', Num2, ' = ', Result)

    elif Oper == "4":
        print("")
        Num1 = float(input("Enter a number: "))
        Num2 = float(input("Enter another number: "))
        print("")
        print("* = Multiply, / = Division, ** = Exponent, // = Floor Division, ! = Factorial")
        print("")
        print("Result: ")
        print("")
        Result = Num1 / Num2
        print(Num1, ' / ', Num2, ' = ', Result)
        # print("Remainder: ")
        # Remainder = Num1 % Num2
        # print(Remainder)
    
    elif Oper == "5":
        print("")
        Num1 = float(input("Enter a number: "))
        Num2 = float(input("Enter another number: "))
        print("")
        print("* = Multiply, / = Division, ** = Exponent, // = Floor Division, ! = Factorial")
        print("")
        print("Result: ")
        print("")
        Result = Num1 ** Num2
        print(Num1, ' ** ', Num2, ' = ', Result)

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

    elif Oper == "7":
        print("")
        Num1 = float(input("Enter a number: "))
        Num2 = float(input("Enter another number: "))
        print("")
        print("* = Multiply, / = Division, ** = Exponent, // = Floor Division, ! = Factorial")
        print("")
        if Num1 < Num2:
          print(Num1, ' < ', Num2, ' = ', "True")

        else:
          print(Num1, ' < ', Num2, ' = ', "False")
        
    elif Oper == "8":
        print("")
        Num1 = float(input("Enter a number: "))
        Num2 = float(input("Enter another number: "))
        print("")
        print("* = Multiply, / = Division, ** = Exponent, // = Floor Division, ! = Factorial")
        print("")
        if Num1 > Num2:
          print(Num1, ' > ', Num2, ' = ', "True")

        else:
          print(Num1, ' > ', Num2, ' = ', "False")

    elif Oper == "9":
        print("")
        Num1 = float(input("Enter a number: "))
        Num2 = float(input("Enter another number: "))
        print("")
        print("* = Multiply, / = Division, ** = Exponent, // = Floor Division, ! = Factorial")
        print("")
        if Num1 == Num2:
          print(Num1, ' is equal to ', Num2)

        else:
          print(Num1, ' is not equal to ', Num2)

    elif Oper == "10":
      def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)
      n = int(input("Input a number to compute the factorial (Numbers from 1 to 997 only): "))
      print("")
      print("* = Multiply, / = Division, ** = Exponent, // = Floor Division, ! = Factorial")
      print("")
      print('Result: ')
      print("")
      print(n, '!', '=', factorial(n))

    else:
      print("Invalid Operation entry, Please try again")
    print("")
    continue2 = input("Do you want to continue (Y / N)? : ")
    