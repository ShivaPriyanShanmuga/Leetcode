class Solution(object):
    def isPowerOfThree(self, n):
        num = 1
        while num < n:
            num *= 3
        if num == n:
            return True
        else:
            return False