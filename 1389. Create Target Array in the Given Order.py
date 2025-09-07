class Solution(object):
    def createTargetArray(self, nums, index):
        t = []
        for i in range(len(nums)):
            t.insert(index[i], nums[i])
        return t