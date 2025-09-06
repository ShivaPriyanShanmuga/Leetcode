class Solution(object):
    def findNumbers(self, nums):
        ct = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                ct += 1
        return ct
        