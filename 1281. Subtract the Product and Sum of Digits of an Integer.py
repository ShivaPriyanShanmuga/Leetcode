class Solution(object):
    def subtractProductAndSum(self, n):
        s = str(n)
        p = 1
        su = 0
        for i in s:
            p *= int(i)
            su += int(i)
        return p - su
        