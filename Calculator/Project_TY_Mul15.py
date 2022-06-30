import math as M
from deep_translator import MyMemoryTranslator
import numpy as np
import qrcode as Q
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import imageio
import scipy.ndimage
import cv2
import googletrans
import pronouncing as pro
from time import time

continue2 = "Y"
while continue2 == "Y":
    print("")
    print("Welcome to Calculator")
    print("")
    Oper = str(input("Enter the operation (1 - Addition, 2 - Subtraction, 3 - Multiply, 4 - Division with Remainder, 5 - Divison without Remainder, 6 - Exponent, 7 - Floor Division, 8 - Less Than, 9 - Greater Than, 10 - Equal, 11 - Factorial, 12 - Square Root, 13 - Cube Root, 14 - Rounding Up, 15 - Rounding Down, 16 - Live Clock, 17 - QR Code, 18 - Abs, 19 - D/R, 20 - R/D, 21 - Sin, 22 - Cos, 23 - Tan, 24 - Asin, 25 - Acos, 26 - Atan, 27 - Log10, 28 - Log, 29 - GCD, 30 - LCM, 31 - HCF, 32 - Add/Subtract Time, 33 - Image to Sketch, 34 - Translator, 35 - Rhyming Words, 36 - WPM Test / Typing Test): "))
    continue3 = "Y"
    
    while continue3 == "Y":    
        if Oper == "1":
            print("")
            Num1 = float(input("Enter a number: "))
            Num2 = float(input("Enter another number: "))
            print("")
            print("Result: ")
            print("")
            Result = Num1 + Num2
            print(Num1, ' + ', Num2, ' = ', Result)
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ").upper()               
    
        elif Oper == "2":
            print("")
            Num1 = float(input("Enter a number: "))
            Num2 = float(input("Enter another number: "))
            print("")
            print("Result: ")
            print("")
            Result = Num1 - Num2
            print(Num1, ' - ', Num2, ' = ', Result)
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ").upper()
    
        elif Oper == "3":
            print("")
            Num1 = float(input("Enter a number: "))
            Num2 = float(input("Enter another number: "))
            print("")
            print("Product: ")
            print("")
            Result = Num1 * Num2
            print(Num1, ' * ', Num2, ' = ', Result)
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ").upper()

        elif Oper == "4":
            print("")
            Num1 = float(input("Enter a number: "))
            Num2 = float(input("Enter another number: "))
            print("")
            print("Result: ")
            print("")
            Result = divmod(Num1, Num2)
            print("The First number is the Quotient and the Second number is the Remainder")
            print(Num1, ' / ', Num2, ' = ', Result)
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ").upper()
        
        elif Oper == "5":
            print("")
            Num1 = float(input("Enter a number: "))
            Num2 = float(input("Enter another number: "))
            print("")
            print("Result: ")
            print("")
            Result = Num1 / Num2
            print(Num1, ' / ', Num2, ' = ', Result)
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ").upper()
            
        elif Oper == "6":
            print("")
            Num1 = float(input("Enter a base: "))
            Num2 = float(input("Enter a power: "))
            print("")
            print("Result: ")
            print("")
            Result = M.pow(Num1, Num2)
            print(Num1, ' ** ', Num2, ' = ', Result)
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ").upper()

        elif Oper == "7":
            print("")
            Num1 = float(input("Enter a number: "))
            Num2 = float(input("Enter another number: "))
            print("")
            print("Result: ")
            print("")
            Result = Num1 // Num2
            print(Num1, ' // ', Num2, ' = ', Result)
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ").upper()

        elif Oper == "8":
            print("")
            Num1 = float(input("Enter a number: "))
            Num2 = float(input("Enter another number: "))
            print("")
            if Num1 < Num2:
                print(Num1, ' < ', Num2, ' = ', "True")
                print("")
                continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ").upper()

            else:
                print(Num1, ' < ', Num2, ' = ', "False")
                print("")
                continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ").upper()
            
        elif Oper == "9":
            print("")
            Num1 = float(input("Enter a number: "))
            Num2 = float(input("Enter another number: "))
            print("")
            if Num1 > Num2:
                print(Num1, ' > ', Num2, ' = ', "True")
                print("")
                continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ").upper()

            else:
                print(Num1, ' > ', Num2, ' = ', "False")
                print("")
                continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ").upper()

        elif Oper == "10":
            print("")
            Num1 = float(input("Enter a number: "))
            Num2 = float(input("Enter another number: "))
            print("")
        
            if Num1 == Num2:
                print(Num1, ' is equal to ', Num2)
                print("")
                continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ").upper()

            else:
                print(Num1, ' is not equal to ', Num2)
                print("")
                continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ").upper()

        elif Oper == "11":
            print("")
            Num1 = int(input("Input a number to compute the factorial (Numbers from 1 to 2147483647 only): "))
            print("")
            Result = M.factorial(Num1)
            print('Result: ')
            print("")
            print(Num1, '!', '=', Result)
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ").upper()

        elif Oper == "12":
            print("")
            Num1 = float(input("What is the number you want to find the square root of? (No Negative numbers): "))
            print("")
            Result = M.sqrt(Num1)
            print("The square root of", Num1, "is", Result )
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ").upper()

        elif Oper == "13":
            print("")
            Num1 = float(input("What is the number you want to find the cube root of? (No Negative numbers): "))
            print("")
            Result = np.cbrt(Num1)
            print("The cube root of", Num1, "is", Result)
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ").upper()

        elif Oper == "14":
            print("")
            Num1 = float(input("Enter a number: "))
            print("")
            Result = M.ceil(Num1)
            print(Num1, "is rounded up to", Result)
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ").upper()

        elif Oper == "15":
            print("")
            Num1 = float(input("Enter a number: "))
            print("")
            Result = M.floor(Num1)
            print(Num1, "is rounded down to", Result)
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ").upper()                   

        elif Oper == "16":
            Time = datetime.now()
            print("")
            print(" It is in Year-Month-Date, Hours: Minutes: Seconds: Milliseconds Format")
            print("")
            print("Live Time:", Time)
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ").upper()

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
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ").upper()

        elif Oper == "18":
            Num1 = float(input("Enter a number: "))
            print("")
            Result = M.fabs(Num1)
            print("")
            print("Result: ", (Result))
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ").upper()        

        elif Oper == "19":
            print("")
            Num1 = float(input("Enter a number: "))
            print("")
            Result = M.radians(Num1)
            print("")
            print("Result: ", Result)
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ").upper()        

        elif Oper == "20":
            print("")
            Num1 = float(input("Enter a number: "))
            print("")
            Result = M.degrees(Num1)
            print("")
            print("Result: ", (Result))
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ").upper()        
       
        elif Oper == "21":
            print("")
            Num1 = float(input("Enter a number: "))
            Result = M.sin(Num1)
            print("")
            print("Result: ", (Result))
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ").upper()        

        elif Oper == "22":
            print("")
            Num1 = float(input("Enter a number: "))
            Result = M.cos(Num1)
            print("")
            print("Result: ", (Result))
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ").upper()        

        elif Oper == "23":
            print("")
            Num1 = float(input("Enter a number: "))
            Result = M.tan(Num1)
            print("")
            print("Result: ", (Result))
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ").upper()        

        elif Oper == "24":
            print("")
            Num1 = float(input("Enter a number: "))
            Result = M.asin(Num1)
            print("")
            print("Result: ", (Result))
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ").upper()        

        elif Oper == "25":
            print("")
            Num1 = float(input("Enter a number: "))
            Result = M.acos(Num1)
            print("")
            print("Result: ", (Result))
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ").upper()        

        elif Oper == "26":
            print("")
            Num1 = float(input("Enter a number: "))
            Result = M.atan(Num1)
            print("")
            print("Result: ", (Result))
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ").upper()        

        elif Oper == "27":
            print("")
            Num1 = float(input("Enter a number: "))
            Result = M.log10(Num1)
            print("")
            print("Result: ", (Result))
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ").upper()       

        elif Oper == "28":
            print("")
            Num1 = float(input("Enter a number: "))
            Num2 = float(input("Enter another number: "))
            Result = M.log(Num2, Num1)
            print("")
            print("Result: ", (Result))
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ").upper()              

        elif Oper == "29":
            print("")
            Num1 = int(input("Enter a number: "))
            Num2 = int(input("Enter another number: "))
            Result = M.gcd(Num2, Num1)
            print("")
            print("Result:", (Result))
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ").upper()     

        elif Oper == "30":
            print("")
            Num1 = int(input("Enter a number: "))
            Num2 = int(input("Enter another number: "))
            Result = M.lcm(Num2, Num1)
            print("")
            print("Result:", (Result))
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ").upper() 

        elif Oper == "31":
            # Function to find HCF the Using Euclidian algorithm
            def compute_hcf(x, y):
                while(y):
                    x, y = y, x % y
                return x

            Num1 = float(input("Enter a number: "))
            Num2 = float(input("Enter another number: "))
            Result = compute_hcf(Num1, Num2)
            print("")
            print("The HCF of", Num1, "and", Num2, "is", Result)
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ").upper()

        elif Oper == "32":
            ## Adding years or months or days or hours or minutes or seconds to datetime
            
            ## Original datetime
            datetime_original = datetime.now()
            print("\nOriginal date: ", datetime_original, "\n")
            print("If you want to subtract time then put - in front of the number", "\n")

            ## Years
            Num7 = int(input("Enter how many years you want to add or subtract: "))
            datetime_new = datetime.now() + relativedelta(years=Num7)
            print("After adding/subtracting years: ", datetime_new, "\n")

            ## Months
            Num6 = int(input("Enter how many months you want to add or subtract: "))
            datetime_new = datetime.now() + relativedelta(months=Num6)
            print("After adding/subtracting months: ", datetime_new, "\n")

            ## Days
            Num5 = int(input("Enter how many days you want to add or subtract: "))
            datetime_new = datetime_new + timedelta(days = Num5)
            print("After adding/subtracting days: ", datetime_new, "\n")

            ## Hours
            Num1 = int(input("Enter how many hours you want to add or subtract: "))
            datetime_new = datetime_new + timedelta(hours = Num1)
            print("After adding/subtracting hours: ", datetime_new, "\n")
            
            ## Minutes
            Num2 = int(input("Enter how many minutes you want to add or subtract: "))
            datetime_new = datetime_new + timedelta(minutes = Num2)
            print("After adding/subtracting minutes: ", datetime_new, "\n")
            
            ## Seconds
            Num3 = int(input("Enter how many seconds you want to add or subtract: "))
            datetime_new = datetime_new + timedelta(seconds = Num3)
            print("After adding/subtracting seconds: ", datetime_new, "\n")
            
            ## Microseconds
            Num4 = int(input("Enter how many milliseconds you want to add or subtract: "))
            datetime_new = datetime_new + timedelta(microseconds = Num4)
            print("After adding/subtracting microseconds: ", datetime_new, "\n")

            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ").upper()

        elif Oper == "33":
            img = "Image-To-Sketch/A.jpg"

            def rgb2gray(rgb):
                return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

            def dodge(front, back):
                final_sketch = front*255/(255-back)
                final_sketch[final_sketch>255]=255
                final_sketch[back==255]=255
                return final_sketch.astype("uint8")

            ss = imageio.imread(img)
            gray = rgb2gray(ss)
            i = 255 - gray
            blur = scipy.ndimage.filters.gaussian_filter(i, sigma=15)
            r = dodge(blur, gray)
            print("")
            img_save = input("Write file name and type: ")
            cv2.imwrite(img_save, r)
            print("")
            print("Sketched Image Got Saved")
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ").upper()

        elif Oper == "34":
            print("")
            print("Number of Supported Languages:", len(googletrans.LANGUAGES)) 
            print(googletrans.LANGUAGES)
            translator = MyMemoryTranslator
            print("")
            to_translate = input("Enter what you want to translate: ")
            print("")
            loc = input("What language are you translating from: ")
            print("")
            des = input("What language do you want to translate into: ")
            print("")
            translated = translator(source=loc, target=des).translate(to_translate)
            print("Here is the translated text:", translated)
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ").upper()

        elif Oper == "35":
            print("")
            InputWord = input("Please Enter a word to find its rhyming words: ")
            print("") 
            ProResult = pro.rhymes(InputWord)  
            print("The rhyming words of the word given by you are: ")
            print("")
            print(ProResult)
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ").upper()

        elif Oper == "36":
            print("")
            # calculate the accuracy of input prompt
            def typingErrors(prompt):
                global iwords

                words = prompt.split()
                errors = 0

                for i in range(len(iwords)):
                    if i in (0, len(iwords)-1):
                        if iwords[i] == words[i]:
                            continue
                        else:
                            errors +=1
                    else:
                        if iwords[i] == words[i]:
                            if (iwords[i+1] == words[i+1]) & (iwords[i-1] == words[i-1]):
                                continue
                            else:
                                errors += 1
                        else:
                            errors += 1
                return errors

            # calculate the speed in words per minute
            def typingSpeed(iprompt, stime, etime):
                global time
                global iwords

                iwords = iprompt.split()
                twords = len(iwords)
                speed = twords / time * 100

                return speed

            # calculate total time elapsed
            def timeElapsed(stime, etime):
                time = etime - stime

                return time

            if __name__ == '__main__':
                prompt = "Physics is the natural science that studies matter, its motion and behavior through space and time, and the related entities of energy and force."
                print("Type this:- '", prompt, "'")

                # listening to input ENTER
                input("press ENTER when you are ready!  ")

                # recording time for input
                stime = time()
                iprompt = input()
                etime = time()

                # gather all the information returned from functions
                time = round(timeElapsed(stime, etime), 2)
                speed = typingSpeed(iprompt, stime, etime)
                errors = typingErrors(prompt)

                # printing all the required data
                print(f"Total Time elapsed: ", time, "s")
                print(f"Your Average Typing Speed was: ", float(str(speed)[:6]), "words / minute")
                print(f"With a total of: ", errors, "errors")
            print("")
            continue3 = input("Do you want to do the same operation again (Y / Type anything if No)? : ").upper()

        else:
            print("Invalid Operation entry, Please try again")
            print("")
       
        if continue3 != "Y":
            print("")
            continue2 = input("Do you want to use the calculator again (Y / N)? : ").upper()

