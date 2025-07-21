class Solution(object):
    def maximumStrongPairXor(self, nums):
        l = []
        for i in nums:
            for j in nums:
                if abs(i - j) <= min(i, j):
                    l.append(i ^ j)
        return max(l)