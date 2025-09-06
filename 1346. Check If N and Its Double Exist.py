class Solution(object):
    def checkIfExist(self, arr):
        for i in arr:
            if (i != 0 and 2 * i in arr) or arr.count(0) >= 2:
                return True
            else:
                pass
        return False
        