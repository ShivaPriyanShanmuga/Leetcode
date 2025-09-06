class Solution(object):
    def countNegatives(self, grid):
        ct = 0
        for i in grid:
            for j in i:
                if j < 0:
                    ct += 1
                else:
                    pass
        return ct