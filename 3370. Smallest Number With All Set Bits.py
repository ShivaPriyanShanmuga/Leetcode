class Solution(object):
    def log(self, i):
        exp = 0
        while i >= 2 ** exp:
            exp += 1
        return exp
    def smallestNumber(self, n):
        if n == 1:
            return 1
        return 2 ** (Solution.log(self, n)) - 1