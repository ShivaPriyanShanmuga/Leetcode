class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()
        p1 = 0
        p2 = 1
        l = len(arr)
        a = []
        while p2 < l:
            a.append(arr[p2] - arr[p1])
            p2 += 1
            p1 += 1
        m = min(a)
        res = []
        for i in range(len(a)):
            if a[i] == m:
                res.append([arr[i], arr[i + 1]])
            else:
                pass
        return res
        