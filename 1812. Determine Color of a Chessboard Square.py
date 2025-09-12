class Solution(object):
    def squareIsWhite(self, coordinates):
        h = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
        su = 0
        su += h[coordinates[0]]
        su += int(coordinates[1])
        return not(su % 2 == 0)