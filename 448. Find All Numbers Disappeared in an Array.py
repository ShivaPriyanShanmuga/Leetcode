class Solution(object):
    def findDisappearedNumbers(self, nums):
        length = len(nums)
        h = {}
        l = []
        for i in range(length):
            h[i+1] = 0
        for i in nums:
            h[i] = 1
        for i in h:
            if h[i] == 0:
                l.append(i)
        return l