class Solution(object):
    def findLucky(self, arr):
        arr.sort()
        arr = arr[::-1]
        for i in arr:
            if i == arr.count(i):
                return i
            else:
                pass
        return -1