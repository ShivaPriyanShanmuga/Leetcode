class Solution(object):
    def findErrorNums(self, nums):
        h = {}
        for i in range(len(nums)):
            h[i+1] = 0
        for i in range(len(nums)):
            h[nums[i]] += 1
        l = []
        for i in h:
            if h[i] == 2:
                l = [i] + l
            elif h[i] == 0:
                l.append(i)

        return l