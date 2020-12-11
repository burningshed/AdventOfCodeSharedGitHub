"""
Library for dealing with grids and paths
"""
# define a path class - which holds its path and current location
# define a gridpoint class which can return distance

import math

class GridPoint:
    """
    GridPoint class for dealing with gridpoints
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def mh_dist(self, OtherPoint=None):
        """
        returns manhatten distance between OtherPoint and this point
        """
        if OtherPoint is None:
            OtherPoint=GridPoint(0,0)
        return abs(OtherPoint.x - self.x) + abs(OtherPoint.y - self.y)
    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)
    def __mul__(self, a):
        return GridPoint(self.x*a, self.y*a)
    def __add__(self, b):
        return GridPoint(self.x+b.x, self.y+b.y)
    def __str__(self):
        return "({},{})".format(self.x, self.y)
    def __round__(self):
        return GridPoint(int(round(self.x)), int(round(self.y)))
    def __hash__(self):
        x = self.x
        y = self.y
        # Cantors Enumeration of Pairs
        n = ((x + y ) * (x + y + 1) / 2) + y
        return int(n)
    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)


class Path:
    """
    Path class to keep track of a history of grid points, maintain both ordered and unordered history
    """
    def __init__(self, start=None):
        if start is None:
            start = GridPoint(0,0)
        self.order_hist = [start]
        self.unorder_hist = set()
        self.unorder_hist.add(start)
    def get_cloc(self):
        """
        get current location (most recent entry in path)
        """
        return self.order_hist[-1]
    def move(self,dvec):
        """
        take dvec (a vector) and move cloc to cloc+dvec
        adding each point along the way to path

        returns 1 if successful, 0 otherwise
        """
        if (dvec.x + dvec.y) == 0:
            return 1
        if not ((dvec.x * dvec.y) == 0):
            print("vector cannot contain both x and y componenets")
            return 0
        dvec = dvec + self.move_step(dvec)
        return self.move(dvec)
    def move_step(self, dvec):
        """
        moves one step in direction of dvec
        """
        if not ((dvec.x * dvec.y) == 0):
            print("vector cannot contain both x and y componenets")
            return 0
        step = round(dvec*(1/abs(dvec)))
        new_cloc = self.get_cloc() + step
        self.order_hist.append(new_cloc)
        self.unorder_hist.add(new_cloc)
        return step*-1
    def __str__(self):
        path_str = ""
        loc_log = ""
        cloc = str(self.get_cloc())
        for ii in range(len(self.order_hist)):
            path_str = str(self.order_hist[ii]) + "<-" + path_str
        for item in self.unorder_hist:
            loc_log += str(item)
        return path_str + "\n" + loc_log + "\n" + cloc
    def findXsections(self, otherPath):
        """
        returns a list of all points at which the two pathes intersect
        """
        return self.unorder_hist & otherPath.unorder_hist
    def get_time_to_point(self, point):
        """
        returns distance to first instance of point
        """
        dist = 0
        for node in self.order_hist:
            if point == node:
                return dist
            dist += 1
        return -1

