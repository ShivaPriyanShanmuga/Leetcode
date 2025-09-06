class Solution(object):
    def findSpecialInteger(self, arr):
        le = len(arr) * 0.25
        for i in arr:
            if arr.count(i) > le:
                return i
            else:
                pass
        