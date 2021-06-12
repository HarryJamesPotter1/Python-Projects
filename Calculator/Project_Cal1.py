continue2 = "Y"
while continue2 == "Y":
    print("")
    Num1 = float(input("Enter a number: "))
    Oper = str(input("Enter the operation (1 - Addition, 2 - Subtraction, 3 - Multiply, 4 - Division, 5 - Exponent, 6 - Floor Division, 7 - Less Than, 8 - Greater Than, 9 - Equal) : "))
    Operation = 0
    Num2 = float(input("Enter another number: "))


    print("")
    print("* = Multiply, / = Division, ** = Exponent, // = Floor Division")
    print("")

    if Oper == "1":
      print("Result: ")
      print("")
      Result = Num1 + Num2
      print(Num1, ' + ', Num2, ' = ', Result)
 
    elif Oper == "2":
      print("Result: ")
      print("")
      Result = Num1 - Num2
      print(Num1, ' - ', Num2, ' = ', Result)
 
    elif Oper == "3":
      print("Product: ")
      print("")
      Result = Num1 * Num2
      print(Num1, ' * ', Num2, ' = ', Result)

    elif Oper == "4":
      print("Result: ")
      print("")
      Result = Num1 / Num2
      print(Num1, ' / ', Num2, ' = ', Result)
      # print("Remainder: ")
      # Remainder = Num1 % Num2
      # print(Remainder)

    elif Oper == "5":
      print("Result: ")
      print("")
      Result = Num1 ** Num2
      print(Num1, ' ** ', Num2, ' = ', Result)

    elif Oper == "6":
      print("Result: ")
      print("")
      Result = Num1 // Num2
      print(Num1, ' // ', Num2, ' = ', Result)

    elif Oper == "7":
        if Num1 < Num2:
          print(Num1, ' < ', Num2, ' = ', "True")

        else:
          print(Num1, ' < ', Num2, ' = ', "False")
        
    elif Oper == "8":
        if Num1 > Num2:
          print(Num1, ' > ', Num2, ' = ', "True")

        else:
          print(Num1, ' > ', Num2, ' = ', "False")

    elif Oper == "9":
        if Num1 == Num2:
          print(Num1, ' is equal to ', Num2)

        else:
          print(Num1, ' is not equal to ', Num2)
          
    else:
      print("Invalid Operation entry, Please try again")
    print("")
    continue2 = input("Do you want to continue (Y / N)? : ")
    