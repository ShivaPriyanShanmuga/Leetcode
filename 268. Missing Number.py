class Solution(object):
    def missingNumber(self, nums):
        for i in range(len(nums) + 1):
            if i in nums:
                pass
            else:
                return i