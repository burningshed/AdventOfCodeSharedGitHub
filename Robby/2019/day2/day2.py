"""
Advent of Code - Day 2 - Intcode-1
"""
import sys
sys.path.insert(0,"..")
import intcode
# Get your puzzle input, and save the file to your computer
# add the path "C:/PATH/to/File.txt" <- Windows or "/PATH/to/File" <- Unix here
FILE_PATH = "day2.in"

# This creates an object that contains all the data in the file you saved
RawInput = open(FILE_PATH, 'r')

# from here you can access the data in a few different ways


# for each line in the file
cur_code = []
for line in RawInput:
    cur_code = line.split(",")
cur_code = [int(x) for x in cur_code]

def day2part1(code):
    code[1] = 12
    code[2] = 2
    p1 = intcode.int_computer(code)
    p1.run_code()
    return p1.get_code()[0]

def day2part2_one_pass(p1, cur_test_code, ans):
    p1.run_code(cur_test_code)
    print(cur_test_code[0])
    if cur_test_code[0] == ans:
        return True
    return False
def day2part2(code, ans):
    found = False
    p1 = intcode.int_computer(code)
    for noun in range(100):
        for verb in range(100):
            new_code = code.copy()
            new_code[1] = noun
            new_code[2] = verb
            found = day2part2_one_pass(p1, new_code, ans)
            if found is True:
                break
        if found is True:
            break
    return noun, verb
ans = 19690720
N,V = day2part2(cur_code, ans)
print("Noun: {}, Verb: {}, Answer: {}".format(N,V,(100*N) + V))
