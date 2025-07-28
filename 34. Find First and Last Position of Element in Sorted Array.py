class Solution(object):
    def searchRange(self, nums, target):
        if target in nums:
            rev = nums[::-1]
            l = []
            l.append(nums.index(target))
            l.append(len(nums) - rev.index(target) - 1)
            return l
        else:
            return [-1, -1]