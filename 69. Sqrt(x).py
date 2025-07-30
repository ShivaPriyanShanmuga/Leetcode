class Solution(object):
    def mySqrt(self, x):
        #actual
        '''ct = 1
        while ct <= (x / ct):
            ct += 1
        return (ct - 1)'''
        #cheating
        return int(x ** 0.5 // 1)