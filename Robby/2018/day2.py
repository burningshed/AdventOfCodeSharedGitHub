inputFile = open("./day2/input")
# build input list in case I need to go through more than once
rawInput = []
class Counter(dict):
    def __missing__(self, key):
        return 0
for line in inputFile:
    rawInput.append(line)
NumCounts = Counter()
for line in rawInput:
    LineLetters = Counter()
    Counted2 = 0
    Counted3 = 0
    for letter in line:
        LineLetters[letter] += 1
    for letter in LineLetters:
        if LineLetters[letter] == 2 and Counted2 == 0:
            NumCounts[2] += 1
            Counted2 = 1
        if LineLetters[letter] == 3 and Counted3 == 0:
            NumCounts[3] += 1
            Counted3 = 1
        if Counted2 == 1 and Counted3 == 1:
            break
print(NumCounts[2] * NumCounts[3])

codeLength = len(rawInput[0])-1
FirstStrike = set()
ZeroStrikes = set(rawInput)
for ii in range(codeLength):
    BadLetters = set()
    ColCounts = Counter()
    for line in ZeroStrikes:
        ColCounts[line[ii]] += 1

    for line in FirstStrike:
        ColCounts[line[ii]] += 1

    for letter in ColCounts:
        if ColCounts[letter] == 1:
            BadLetters.add(letter)

    toRemove = set()
    for line in FirstStrike:
        if line[ii] in BadLetters:
            toRemove.add(line)
    for line in toRemove:
        FirstStrike.remove(line)
    toRemove = set()
    for line in ZeroStrikes:
        if line[ii] in BadLetters:
            toRemove.add(line)
    for line in toRemove:
        ZeroStrikes.remove(line)
        FirstStrike.add(line)

WorkingSet = FirstStrike | ZeroStrikes
PosAns = WorkingSet
for line in WorkingSet:
    DiffCounts = Counter()
    for ii in range(codeLength):
        for code in PosAns:
            if line[ii] != code[ii]:
                DiffCounts[code] += 1
    # seek through each code
    for code in PosAns:
        if DiffCounts[code] == 1:
            print("Found it!", code, line)
            for ii in range(codeLength):
                if code[ii] == line[ii]:
                    print(code[ii])





