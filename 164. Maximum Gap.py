class Solution(object):
    def maximumGap(self, nums):
        nums.sort()
        m = 0
        for i in range(len(nums)):
            if i == len(nums) - 1:
                pass
            elif nums[i + 1] - nums[i] > m:
                m = nums[i + 1] - nums[i]
            else:
                pass
        return m