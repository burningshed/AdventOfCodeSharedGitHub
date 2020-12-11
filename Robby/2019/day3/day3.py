"""
Advent of Code 2019 - Day 3
"""
from grid_tools import GridPoint, Path
import sys
sys.setrecursionlimit(1500)
# Get your puzzle input, and save the file to your computer
# add the path "C:/PATH/to/File.txt" <- Windows or "/PATH/to/File" <- Unix here
FILE_PATH = "day3.in"

# This creates an object that contains all the data in the file you saved
RawInput = open(FILE_PATH, 'r')

# from here you can access the data in a few different ways

# If it is text seperated by newlines

# for each line in the file
D_key = {
    "R": GridPoint(1, 0),
    "U": GridPoint(0, 1),
    "L": GridPoint(-1, 0),
    "D": GridPoint(0, -1)
}
wires = []
for line in RawInput:
    # print that line
    wires.append(line.rstrip().split(","))

sLoc = GridPoint(0, 0)
paths = []

for wire in wires:
    paths.append(Path(sLoc))
    for stage in wire:
        dvec = D_key[stage[0]]*int(stage[1:])
        paths[-1].move(dvec)
Xing = paths[0].findXsections(paths[1])
mhDists = []
lowDist = 0
for item in Xing:
    mhDists.append(item.mh_dist())
    if lowDist == 0:
        lowDist = item.mh_dist()
    else:
        if (item.mh_dist() < lowDist) and (item.mh_dist != 0):
            lowDist = item.mh_dist()
print("Answer to Part 1: {}".format(lowDist))
lowTime = 0
for item in Xing:
    curTime = (paths[0].get_time_to_point(item)
               + paths[1].get_time_to_point(item))
    if lowTime == 0:
        lowTime = curTime
    else:
        if (curTime < lowTime) and (curTime != 0):
            lowTime = curTime
print("Answer to Part 2: {}".format(lowTime))
