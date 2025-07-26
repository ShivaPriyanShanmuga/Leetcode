class Solution(object):
    def reverse(self, x):
        t = 0
        if x >= 0:
            t = int(str(x)[::-1])
        else:
            t = - int(str(abs(x))[::-1])
        
        if - 2 ** 31 <= t < 2 ** 31:
            return t
        else:
            return 0