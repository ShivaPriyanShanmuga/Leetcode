class Solution(object):
    def isPowerOfTwo(self, n):
        if n == 1:
            return True
        elif n < 1:
            return False
        else:
            return Solution.isPowerOfTwo(self, float(n) / 2)