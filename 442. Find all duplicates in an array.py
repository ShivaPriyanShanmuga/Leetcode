class Solution(object):
    def findDuplicates(self, nums):
        l = []
        h = {}
        for i in nums:
            if i in h and h[i] == 1:
                h[i] += 1
                l.append(i)
            elif i in h:
                pass
            else:
                h[i] = 1
        return l