"""
tests for lib files
"""
import grid_tools

class GridPointTests:
    def __init__(self):
        self.a = GridPoint(0,0)
        self.b = GridPoint(3,2)
        self.c = GridPoint(-2,2)
        self.d = GridPoint(3,-1)
        self.e = GridPoint(-4,-4)
    def mh_dist_test(self):
        print("Test 1 (Normal): {}]".format(self.a.mh_dist(self.b)==5))
        print("Test 2 (Negative Numbers): {}]".format(self.a.mh_dist(self.e)==8))
        print("Test 3 (Using Default Argument): {}]".format(self.b.mh_dist()==5))
        print("Test 4 (Two Non-Zero Points): {}]".format(self.b.mh_dist(self.c)==9))
        print("Test 5 (Mixed Signs): {}]".format(self.c.mh_dist(self.d)==8))
    def test_addition(self):
        print("Test 1 (Both Positve): {}".format(a+b))

test = GridPointTests()
test.mh_dist_test()
test.test_addition()
