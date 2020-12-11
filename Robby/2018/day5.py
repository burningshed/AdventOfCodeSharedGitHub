import numpy as np

class Counter(dict):
    def __missing__(self, key):
        return 0
#
def removeReact(index, Chain):
    return Chain[:index-1] + Chain[index+1:]
rawInput = open("./day5/input", "r")
print("Starting")
InPolymerChain = rawInput.readline()
def reactor(polymerChain):
    RpolymerChain = polymerChain[:]
    Done = False
    while not Done:
        Done = True
        prev = ""
        prevCap = ""
        ii = -1
        workingChain = RpolymerChain[:]
        for polymer in workingChain:
            ii = ii + 1
            curCap = (polymer.upper() == polymer)
            if (polymer.upper() == prev.upper()) and (curCap != prevCap):
                RpolymerChain = removeReact(ii, RpolymerChain)
                Done = False
                prevCap = ""
                prev = ""
                break
            prevCap = curCap
            prev = polymer
    return(RpolymerChain)
rawInput.close()

ChainA = reactor(InPolymerChain)
MinLen = len(ChainA)
Lang = set()
for letter in ChainA:
    Lang.add(letter.upper())
for symb in Lang:
    curChain = ChainA.replace(symb, "")
    curChain = curChain.replace(symb.lower(),"")
    curChain = reactor(curChain)
    if len(curChain) < MinLen:
        MinLen = len(curChain)
        MinChain = curChain
print(MinLen)
