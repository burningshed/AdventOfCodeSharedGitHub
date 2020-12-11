"""
Advent of Code - 2019 - Day 4

Finding a password
Rules:
- 6 digit number
- Puzzle input is range of possible values
- Two adjacent digits are the same
- left to right, digits never decrease

How many different possible passwords are there?
"""
from collections import defaultdict
PUZZLE_INPUT_TUP = ((1, 3, 4, 7, 9, 2), (6, 7, 5, 8, 1, 0))
PUZZLE_INPUT_STR = ("134792", "675810")

POSS_DIGITS = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# Idea 1: tree, key is the int, value is a list of possible next entries


def construct_pass(key, choice):
    password = str(key) + str(choice)
    return password


class Password_Digit_LR:
    def __init__(self, poss_keys, poss_vals):
        """
        creates dict, keys are digits to left, values are poss digits to right
        """
        self.Poss_Tree = {x: list(POSS_DIGITS) for x in poss_keys}
        self.place = len(str(poss_keys[0]))

    def trim_range(self, low_bound, hi_bound, full_bound=True):
        """
        trims current digit possible values/keys to fit within provided range
        if full_bound=True, only considers first [place] digits of bounds
        """
        low_bound_int = int(low_bound[:self.place+1])
        hi_bound_int = int(hi_bound[:self.place+1])

        # Remove keys outside of range
        # modifying dict during loop caused lots of problems - del after loop
        keys_to_del = []
        for key in self.Poss_Tree:
            if key < int(low_bound[:self.place]):
                keys_to_del.append(key)
                continue
            elif key > int(hi_bound[:self.place]):
                keys_to_del.append(key)
                continue
        for key in keys_to_del:
            del self.Poss_Tree[key]

        # Remove values outside of range
        vals_to_del = defaultdict(list)
        for key in self.Poss_Tree:
            for choice in self.Poss_Tree[key]:
                password = int(construct_pass(key, choice))
                if password > hi_bound_int or password < low_bound_int:
                    vals_to_del[key].append(choice)
        for key in vals_to_del:
            for val in vals_to_del[key]:
                self.Poss_Tree[key].remove(val)

    def trim_decreasing_digits(self):
        """
        ensure all values for each key are not decreasing
        """
        vals_to_del = defaultdict(list)
        for key in self.Poss_Tree:
            for choice in self.Poss_Tree[key]:
                if choice < int(str(key)[-1]):
                    vals_to_del[key].append(choice)
        for key in vals_to_del:
            for val in vals_to_del[key]:
                self.Poss_Tree[key].remove(val)
    def get_next_keys(self):
        """
        return list of currently valid keys for use in next digit
        """
        P_List = []
        for key in self.Poss_Tree:
            for choice in self.Poss_Tree[key]:
                P_List.append(int(construct_pass(key, choice)))
        return P_List

    def get_next_conf_keys(self):
        """
        return list of passwords that are known to be valid
        (that is, last digit of key and val are equal)
        """
        C_List = []
        for key in self.Poss_Tree:
            key_c = int(str(key)[-1])
            for choice in self.Poss_Tree[key]:
                if choice == key_c:
                    C_List.append(int(construct_pass(key, choice)))
        return C_List
    def get_next_unconf_keys(self):
        """
        return list of passwords that might be valid
        last digit of key and val are not equal
        """
        UC_List = []
        for key in self.Poss_Tree:
            key_c = int(str(key)[-1])
            for choice in self.Poss_Tree[key]:
                if choice != key_c:
                    UC_List.append(int(construct_pass(key, choice)))
        return UC_List


def passgen_step(bounds, unconf_keys, conf_keys=[]):
    """
    min_val/max_val are the lower and upper bounds of possible passwords
    conf_keys are passwords known to be valid (contain a repeated pair)
    unconf_keys might be valid - but do not yet have a repeated pair
    """
    # Generate digit class from unconfirmed keys
    D1 = Password_Digit_LR(unconf_keys, POSS_DIGITS)
    D1.trim_range(*bounds)
    D1.trim_decreasing_digits()
    # if confirmed keys exist, generate digit class from those
    if conf_keys != []:
        CD1 = Password_Digit_LR(conf_keys, POSS_DIGITS)
        CD1.trim_range(*bounds)
        CD1.trim_decreasing_digits()
        conf_pass = CD1.get_next_keys()
    else:
        conf_pass = []
    unconf_pass = D1.get_next_unconf_keys()
    conf_pass.extend(D1.get_next_conf_keys())
    return unconf_pass, conf_pass


def passgen(bounds):
    curDigit = 2
    maxDigits = len(bounds[1])
    D1 = passgen_step(bounds, POSS_DIGITS)
    while curDigit < maxDigits:
        D1 = passgen_step(bounds, *D1)
        curDigit += 1
    return D1


def tests_Part1(test='a'):
    D1 = Password_Digit_LR(POSS_DIGITS, POSS_DIGITS)
    if test in "a1":
        testBounds = ("14", "74")
        print("Starting Passwords:")
        print(D1.get_next_keys())
        D1.trim_range(*testBounds)

        print("\nRanged Passwords:")
        print(D1.get_next_keys())

        D1.trim_decreasing_digits()
        print("\nIncreasing Passwords:")
        print(D1.get_next_keys())

    if test in 'a2':
        testBounds = ("144", "794")
        D1.trim_range(*testBounds)
        D1.trim_decreasing_digits()
        D2keys = D1.get_next_keys()
        print("Input for 2nd Iteration: ")
        print(D2keys)
        D2 = Password_Digit_LR(D2keys, POSS_DIGITS)
        D2.trim_range(*testBounds)
        D2.trim_decreasing_digits()
        print(D2.get_next_keys())
        print("Confirmed Passwords")
        print(D2.get_next_conf_keys())
        print("Unconfirmed Passwords")
        print(D2.get_next_unconf_keys())

    if test in "a34":
        print("Testing passgen_step():\n\n")
        testBounds = ("144", "756")
        D1 = passgen_step(testBounds, POSS_DIGITS)
        print(D1)
        D2 = passgen_step(testBounds, *D1)
        print(D2)

    if test in 'a4':
        print("\n\nTesting passgen()")
        D3 = passgen(testBounds)
        print(D3[1])
    if test in 'a5':
        testBounds = ("14444", "56431")
        D1 = passgen(testBounds)
        print(len(D1[1]))


def day4_part1(bounds):
    D1 = passgen(bounds)
    return D1[1]

def check_pass(password):
    """
    checks password for chains of repeated characters
    if any chain is greater then 2, returns result of
    surrounding substrings.

    if no chain of length 2, returns False
    if chain of exactly 2, returns True
    """
    # big_chain : length of longest chain of repeated symbols
    # c_start : index at which big_chain starts
    big_chain = 0
    cur_loc = 0
    for symb in password:
        if big_chain == 0:
            l_symb = symb
            cur_chain = 1
            big_chain = 1
            c_start = 0
            cur_c = cur_loc
            cur_loc += 1
            continue
        if symb == l_symb:
            cur_chain += 1
        else:
            cur_chain = 1
            cur_c = cur_loc
        if cur_chain > big_chain:
            big_chain = cur_chain
            c_start = cur_c
        cur_loc += 1
        l_symb = symb

    # return or repeat, need big_chain, c_start
    if big_chain < 2:
        return False
    if big_chain == 2:
        return True
    return (check_pass(password[:c_start])
            or check_pass(password[c_start+big_chain:]))


def day4_part2(p1_ans):
    # for each password
    # - find longest chain
    # - if 2, done, password is good
    # - if >2, repeat with substrings before and after chain
    # - if either result passes, password passes
    p1_ans = [str(x) for x in p1_ans]
    p2_ans = []
    for pword in p1_ans:
        if check_pass(pword):
            p2_ans.append(pword)
    return p2_ans


def testd4p2():
    TestInput = [
        "112233",
        "123444",
        "111122",
        "122233",
        "222222",
        "112222",
        "111345"
    ]
    test_ans = day4_part2(TestInput)
    print(test_ans)


d4p1 = day4_part1(PUZZLE_INPUT_STR)
print("Part 1 Answer: ", len(d4p1))
print("Part 2 Answer: ", len(day4_part2(d4p1)))

