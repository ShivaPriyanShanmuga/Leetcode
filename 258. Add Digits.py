class Solution(object):
    def addDigits(self, num):
        if num < 10:
            return num
        else:
            s = str(num)
            sc = ' '.join(s)
            return Solution.addDigits(self, sum(map(int, sc.split())))
        