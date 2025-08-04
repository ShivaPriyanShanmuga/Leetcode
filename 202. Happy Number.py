class Solution(object):
    def isHappy(self, n):
        l = []
        while n != 1:
            s = str(n)
            su = 0
            for i in s:
                su += (int(i) ** 2)
            if su in l:
                return False
            else:
                l.append(n)
                n = su
        return True