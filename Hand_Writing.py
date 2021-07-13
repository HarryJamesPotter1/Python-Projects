import pywhatkit as kit

text = input("Enter the text here: ")

kit.text_to_handwriting(text, "handwriting.jpg", [0,0,0])