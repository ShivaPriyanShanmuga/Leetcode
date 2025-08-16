class Solution(object):
    def thirdMax(self, nums):
        max3 = max(nums)
        while max3 in nums:
            nums.remove(max3)
        if nums == []:
            return max3
        max2 = max(nums)
        while max2 in nums:
            nums.remove(max2)
        if nums == []:
            return max3
        return max(nums)