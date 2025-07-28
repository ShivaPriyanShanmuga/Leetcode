class Solution(object):
    def removeElement(self, nums, val):
        ct = nums.count(val)
        while ct > 0:
            nums.remove(val)
            ct -= 1
        return len(nums)