"""
Library for dealing with grids and paths
"""
# define a path class - which holds its path and current location
# define a gridpoint class which can return distance

class GridPoint:
    """
    GridPoint class for dealing with gridpoints
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def mh_dist(self, OtherPoint=GridPoint(0,0)):
        """
        returns manhatten distance between OtherPoint and this point
        """
        return abs(OtherPoint.x - self.x) + abs(OtherPoint.y - self.y)
    
    def __add__(self, b):
        return GridPoint(self.x+b.x, self.y+b.y)
    def __str__(self):
        return "({}.{})".format(self.x, self.y)

class Path:
    """
    Path class to keep track of a history of grid points, maintain both ordered and unordered history
    """
    def __init__(self, start=GridPoint(0,0)):
        self.order_hist = [start]
        self.unorder_hist = set(start)
    def get_cloc(self):
        return self.order_hist[-1]

