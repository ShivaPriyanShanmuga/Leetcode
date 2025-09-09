class Solution(object):
    def numIdenticalPairs(self, nums):
        ct = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    ct += 1
                else:
                    pass
        return ct