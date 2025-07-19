class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        sum = 0
        for i in range(len(nums)):
            if bin(i)[2:].count('1') == k:
                sum += nums[i]
        return sum
        