import time
import numpy as np
import numpy.linalg as nla

rawInput = open("./day4/input")

class GaurdCounter(dict):
    def __missing__(self, key):
        return np.array([0]*60)
#
# [1518-07-10 00:59] wakes up
ledger = []
GaurdRecords = GaurdCounter()
for event in rawInput:
    parsing = event.split("]")
    datetime = time.strptime(parsing[0], "[%Y-%m-%d %H:%M")
    ledger.append((datetime,parsing[1]))
ledger.sort(key=lambda entry: entry[0])
curDay = 0
for entry in ledger:
    if entry[1][1] == 'G':
        curDay += 1
        curIDnum = entry[1].split()
        curIDnum = int(curIDnum[1][1:])
    if entry[1][1] == 'f':
        asleepAt = entry[0]
    if entry[1][1] == 'w':
        
        awakeFor = entry[0][4] - asleepAt[4]
        night = np.array([0]*60)
        night[asleepAt[4]:entry[0][4]] = 1
        GaurdRecords[curIDnum] += night
MostSleep = [0,0]
for gaurd in GaurdRecords:
    curTotal = np.sum(GaurdRecords[gaurd])
    if curTotal > MostSleep[0]:
        MostSleep = [curTotal, gaurd]
print(MostSleep)
BigMin = np.argmax(GaurdRecords[MostSleep[1]])
print(BigMin)
print(GaurdRecords[MostSleep[1]])
print(BigMin * MostSleep[1])

BigMin = 0
MinSize = 0
for gaurd in GaurdRecords:
    curSize = nla.norm(GaurdRecords[gaurd], np.inf)
    if curSize > MinSize:
        BigMin = np.argmax(GaurdRecords[gaurd])
        MinSize = curSize
        curOut = BigMin * gaurd
print(curOut)
