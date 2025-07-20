class Solution(object):
    def hasTrailingZeros(self, nums):
        for i in range(len(nums)):
            nums[i] = bin(nums[i])
        lst = []
        for i in nums:
            if i[-1] == '0':
                lst.append(i)
        return len(lst) > 1