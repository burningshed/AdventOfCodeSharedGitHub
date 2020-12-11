"""
Multiple puzzles this year use "intcode" this library will be used to work with those codes
"""

from collections import defaultdict

"""
define possible operation codes, and corresponding operations -
note: writing the dictionary out would have been clearer actually
"""






class int_computer():
    """
    operates on intcodes per Advent of Code 2019 - Day 2
    """
    def __init__(self, init_code):
        """
        Initialize with some intcode
        """
        self.code = init_code
        self.pointer = 0
        self.OP_DICT = {
            1: self.intcode_add,
            2: self.intcode_mult,
            3: self.intcode_get_input,
            4: self.intcode_get_output,
            99: self.intcode_quit
        }
 
    def intcode_add(self, *argv):
        """
        moves pointer 4 positions forward, adds positions 1 and 2,
        outputs position 3
        """
        STEP_SIZE = 4
        in1 = int(self.code[self.pointer+1])
        in2 = int(self.code[self.pointer+2])

        argd = defaultdict(lambda: False)
        argd.update(enumerate(argv))
        if not argd[0]:
            in1 = int(self.code[in1])
        if not argd[1]:
            in2 = int(self.code[in2])
        result = in1 + in2
        if not argd[2]:
            out1 = int(self.code[self.pointer+2])
            self.code[out1] = str(result)
        else:
            self.code[self.pointer+2] = str(result)
        self.pointer += STEP_SIZE
        return 1

    def intcode_mult(self, *argv):
        """
        moves pointer 4 positions forward, multiplies positions 1 and 2,
        outputs position 3
        """
        STEP_SIZE = 4
        in1 = int(self.code[self.pointer+1])
        in2 = int(self.code[self.pointer+2])
        argd = defaultdict(lambda: False)
        argd.update(enumerate(argv))
        if not argd[0]:
            in1 = int(self.code[in1])
        if not argd[1]:
            in2 = int(self.code[in2])
        result = in1 * in2
        if not argd[2]:
            out1 = int(self.code[self.pointer+2])
            self.code[out1] = str(result)
        else:
            self.code[self.pointer+2] = str(result)
        self.pointer += STEP_SIZE
        return 1

    def intcode_get_input(self, *argv):
        status = 1
        return status

    def intcode_get_output(self, *argv):
        status = 1
        return status

    def intcode_quit(self, *argv):
        return 0

   
    def run_step(self):
        """
        perform one operation,
        """
        instruction_str = self.code[self.pointer]
        opcode = instruction_str[-2:]
        # define argd here
        # default
        args = "110"
        status = self.OP_DICT[int(opcode)](*args)
        return status

    def run_code(self):
        """
        run through intcode, if no code is provided use the code provided when class was created
        returns 0 if 99 was reached, 2 if some unexpected op-code encountered
        """
        retVal = 1
        while(retVal == 1):
            retVal = self.run_step()
        return retVal

    def get_code(self):
        return self.code


if __name__ == "__main__":
    # Test case for day 2 - testing addition, multiplication, quitting
    testCase2 = int_computer(
        ["1", '9', '10', '3', '2', '3', '11', '0', '99', '30', '40', '50'])
    # test case testing simple quiting, addition
    testCase1 = int_computer(["1", "1", "1", "1", "99"])
    # test case testing parsing of opcode args
    testCase3 = int_computer(["00001", "1", "1", "1",
                              "11101", "1", "1", "1",
                              "1002", "12", "3", "12",
                              "33"])
    print(testCase1.get_code())
    print(testCase1.run_code())
    print(testCase1.get_code())
    #testCase.run_step()

    print(testCase2.get_code())
    print(testCase2.run_code())
    print(testCase2.get_code())

    print(testCase3.get_code())
    print(testCase3.run_code())
    print(testCase3.get_code())
