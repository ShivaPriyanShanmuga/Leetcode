class Solution(object):
    def addToArrayForm(self, num, k):
        s = ''
        for i in num:
            s += str(i)
        n = str(int(s) + k)
        s = []
        for i in n:
            s.append(int(i))
        return s