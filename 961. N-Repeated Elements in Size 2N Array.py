class Solution(object):
    def repeatedNTimes(self, nums):
        for i in nums:
            if nums.count(i) != 1:
                return i
            else:
                pass
        