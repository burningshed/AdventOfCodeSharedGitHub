"""
Docstring - This explains what the file does
This is a starter template that reads data in from a file
"""

# Get your puzzle input, and save the file to your computer
# add the path "C:/PATH/to/File.txt" <- Windows or "/PATH/to/File" <- Unix here
FILE_PATH = ""

# This creates an object that contains all the data in the file you saved
RawInput = open(FILE_PATH, 'r')

# from here you can access the data in a few different ways

# If it is text seperated by newlines

# for each line in the file
for line in RawInput:
    # print that line
    print(line)

# note that if the text is not seperated by newlines line will take the value of each character in the string
