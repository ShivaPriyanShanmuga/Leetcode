class Solution(object):
    def isPowerOfFour(self, n):
        i = 0
        while 4 ** i < n:
            i += 1
        if 4 ** i == n:
            return True
        else:
            return False