"""
Advent of Code 2019 - Day 5
Update Intcode
Add opcodes:
3 (single integer input, store at location provided)
4 (outputs value stored at location)

Parameter Modes
mode 0 - parameters are position
mode 1 - immediate mode - parameters are values

first instruction is not PPPOO where Ps are parameter modes (one for each parameter) and Os are the 2 digit opcodes
"""
PUZZLE_INPUT = "./day5.in"
input = open(PUZZLE_INPUT, 'r')
for line in input:
    code = line.split(',')
print(code)
