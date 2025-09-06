class Solution(object):
    def cnt(self, i, nums):
        ct = 0
        for j in nums:
            if j < i:
                ct += 1
            else:
                pass
        return ct
    def smallerNumbersThanCurrent(self, nums):
        fin = []
        for i in nums:
            fin.append(Solution.cnt(self, i, nums))
        return fin
        