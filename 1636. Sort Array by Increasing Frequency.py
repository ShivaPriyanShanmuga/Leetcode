class Solution(object):
    def frequencySort(self, nums):
        h = {}
        ct = []
        for i in nums:
            c = nums.count(i)
            if c in h:
                h[c].append(i)
            else:
                h[c] = [i]
                ct.append(c)
        ct.sort()
        arr = []
        for i in ct:
            h[i].sort(reverse=True)
            arr.extend(h[i])
        return arr