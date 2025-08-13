class Solution(object):
    def moveZeroes(self, nums):
        ct = nums.count(0)
        while ct != 0:
            nums.remove(0)
            nums.append(0)
            ct -= 1
        return nums