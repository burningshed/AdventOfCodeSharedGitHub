"""
Advent of Code 2019 - Day 1

Fuel = (mass / 3) round down, - 2
"""

# Get your puzzle input, and save the file to your computer
# add the path "C:/PATH/to/File.txt" <- Windows or "/PATH/to/File" <- Unix here
FILE_PATH = "day1.in"

# This creates an object that contains all the data in the file you saved
RawInput = open(FILE_PATH, 'r')

# from here you can access the data in a few different ways

# If it is text seperated by newlines

# for each line in the file
#modMasses = []
def fuelFuel(x):
    y = int(x/3)-2
    if y <= 0:
        return 0
    return y + fuelFuel(y)
totFuel = 0
totFuelFuel = 0
for line in RawInput:
    # print that line
 #   modMasses.append(line.rstrip())
    startFuel = int(int(line.rstrip())/3)-2
    totFuelFuel += startFuel + fuelFuel(startFuel)
    totFuel += startFuel

#print(modMasses)
print("Part 1: {}".format(totFuel))
print("Part 2: {}".format(totFuelFuel))
# note that if the text is not seperated by newlines line will take the value of each character in the string
