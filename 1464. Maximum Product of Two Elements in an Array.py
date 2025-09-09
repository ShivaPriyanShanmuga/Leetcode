class Solution(object):
    def maxProduct(self, nums):
        m1 = max(nums)
        nums.pop(nums.index(m1))
        m2 = max(nums)
        nums.pop(nums.index(m2))
        return (m1 - 1) * (m2 - 1)
        