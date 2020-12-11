import numpy as np
def ManhDist(point1, point2):
    """
    returns the "Manhattan" or "Taxi-Cab" distance between two points
    """
    a = np.abs(point1[0] - point2[0])
    b = np.abs(point1[1] - point2[1])
    return a + b

fp = open("./day6/input", 'r')


coords = []
for line in fp:
    nextPoint = line.split(", ")
    coords.append([int(nextPoint[0]),int(nextPoint[1])])
coords = np.array(coords)

#print(coords)
"""
size = np.amax(coords, 0)
grid = np.zeros(size+(1,1))
Done = False
label = 1
for coord in coords:
    grid[coord[0]][coord[1]] = label
    label += 1
maxLabel = label
print(len(grid))
nextGrid = np.copy(grid)
while not Done:
    grid = np.copy(nextGrid)
    print("At Top")
    for label in range(maxLabel):
        loc = np.where(grid == label)
        try:
            if nextGrid[loc[0][0] + 1][loc[1][0]] == 0:
                nextGrid[loc[0][0] + 1][loc[1][0]] = label
            if nextGrid[loc[0][0] + 1][loc[1][0]] < label:
                nextGrid[loc[0][0] + 1][loc[1][0]] = 'X'
        except:
            print("oh")
            #do nothing
        try:
            if nextGrid[loc[0][0] - 1][loc[1][0]] == 0:
                nextGrid[loc[0][0] - 1][loc[1][0]] = label
            if nextGrid[loc[0][0] - 1][loc[1][0]] < label:
                nextGrid[loc[0][0] - 1][loc[1][0]] = 'X'
        except:
            print("oh")
            #do nothing

        try:
            if nextGrid[loc[0][0]][loc[1][0] -1] == 0:
                nextGrid[loc[0][0]][loc[1][0] -1] = label
            if nextGrid[loc[0][0]][loc[1][0] -1] < label:
                nextGrid[loc[0][0]][loc[1][0] -1] = 'X'
        except:
            print("oh")
            #do nothing

        try:
            if nextGrid[loc[0][0]][loc[1][0] +1] == 0:
                nextGrid[loc[0][0]][loc[1][0] +1] = label
            if nextGrid[loc[0][0]][loc[1][0] +1] < label:
                nextGrid[loc[0][0]][loc[1][0] +1] = 'X'
        except:
            print("oh")
            #do nothing

    print(np.any(grid - nextGrid))
    if not np.any(nextGrid - grid):
        Done = True
print(grid)
"""
