class Solution(object):
    def runningSum(self, nums):
        fin = []
        s = 0
        for i in nums:
            s += i
            fin.append(s)
        return fin
        