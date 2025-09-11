class Solution(object):
    def trimMean(self, arr):
        arr.sort()
        t = len(arr) // 20
        for i in range(t):
            arr.pop(0)
            arr.pop()
        n = len(arr)
        return float(sum(arr)) / n
        