"""
Day 3
of adventofcode
"""
class Counter(dict):
    """
Counter is a dictionary that returns 0 when accessing a non-existant key
    """
    def __missing__(self, key):
        return 0
class Lister(dict):
    """
Lister is a dictionary that returns an empty list when accessing a non-existant key
    """
    def __missing__(self, key):
        return []

Fabric = Counter()
Claims = Lister()
posAns = set()

# Open input file
RawInput = open("./day3/input", 'r')

# Each Line has following format:
# #1 @ 1,1: 1x1
for line in RawInput:
    # split line by whitespace
    claim = line.split()
    # add current claim to possible correct answers
    posAns.add(claim[0])

    # pull starting location out of claim, remove trailing ':'
    claimLoc = claim[2].split(',')
    claimLoc[1] = int(claimLoc[1][:-1])
    claimLoc[0] = int(claimLoc[0])
    # pull size of claim out
    claimSize = claim[3].split('x')
    claimSize[0] = int(claimSize[0])
    claimSize[1] = int(claimSize[1])
    # store the starting location for later reference
    orgLoc = claimLoc[:]
    for ii in range(claimSize[0]):
        # reset to start of row
        claimLoc[1] = orgLoc[1]
        for jj in range(claimSize[1]):
            # add 1 to count of claims at claimLoc
            Fabric[tuple(claimLoc)] += 1
            # append claim to list (set is unnessessary since each claim can only occur at any locaiton once)
            CurSpot = Claims[tuple(claimLoc)]
            CurSpot.append(claim[0])
            Claims[tuple(claimLoc)] = CurSpot
            # increment location
            claimLoc[1] += 1
        claimLoc[0] += 1

overlap = 0
for square in Fabric:
    if Fabric[square] > 1:
        overlap += 1
        for elf in Claims[square]:
            if elf in posAns:
                posAns.remove(elf)
print(overlap)
print(posAns)


