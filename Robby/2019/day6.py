"""
Docstring - This explains what the file does
This is a starter template that reads data in from a file
"""

# Get your puzzle input, and save the file to your computer
# add the path "C:/PATH/to/File.txt" <- Windows or "/PATH/to/File" <- Unix here
FILE_PATH = "day6.in"

# This creates an object that contains all the data in the file you saved
RawInput = open(FILE_PATH, 'r')

# from here you can access the data in a few different ways

# If it is text seperated by newlines




# for each line in the file
sats = []
for line in RawInput:
    line = line.rstrip()
    orbitee, orbitor = line.split(')')
    sats.append((orbitee,orbitor))
print(len(sats))
def findCores(satList):
    cores = set()
    leaves = set()
    for satPair in satList:
        cores.add(satPair[0])
        leaves.add(satPair[1])
    for ele in leaves:
        cores.discard(ele)
    return cores
def countOrbs(satList, depth):
    cores = findCores(satList)
    newSatList = []
    for satPair in satList:
        if satPair[0] not in cores:
            newSatList.append(satPair)
    if len(newSatList) > 0:
        return len(cores)*depth + countOrbs(newSatList, depth + 1)
    return len(cores) * depth
orbs = countOrbs(sats, 0)
print(orbs)


# note that if the text is not seperated by newlines line will take the value of each character in the string
