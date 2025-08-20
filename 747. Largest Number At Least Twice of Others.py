class Solution(object):
    def dominantIndex(self, nums):
        m = max(nums)
        ind = nums.index(m)
        nums.remove(m)
        if m >= 2 * max(nums):
            return ind
        else:
            return -1