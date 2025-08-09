class Solution(object):
    def containsDuplicate(self, nums):
        has = {}
        for i in nums:
            if i in has:
                return True
            else:
                has[i] = 1
        return False