class Solution(object):
    def singleNumber(self, nums):
        l = nums
        if l[0] in l[1:]:
            t = l[1:]
            t.remove(l[0])
            Solution.singleNumber(self, t)
        else:
            return l[0]
