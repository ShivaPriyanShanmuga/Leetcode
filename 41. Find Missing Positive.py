class Solution(object):
    def firstMissingPositive(self, nums):
        for i in range(len(nums)):
            while 1 <= nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        for i in range(len(nums)):
            if nums[i] == i + 1:
                pass
            else:
                return i + 1
        return len(nums) + 1