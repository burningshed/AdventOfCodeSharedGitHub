# part 2
def freqSolver(start, change):
    return start + change
Freq = 0
inputFile = open("./day1/inputs")
CurChange = 0
FreqSet = {Freq}
ChangeList = []
for line in inputFile:
    ChangeList.append(line)
notDone = True
while notDone:
    for line in ChangeList:
        if line[0] == "+":
            CurChange = int(line[1:])
        else:
            CurChange = -int(line[1:])

        Freq = freqSolver(Freq, CurChange)
        if Freq in FreqSet:
            print("Found! Freq = {}". format(Freq))

            notDone = False
            break
        FreqSet.add(Freq)


