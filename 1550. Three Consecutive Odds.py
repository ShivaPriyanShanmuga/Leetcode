class Solution(object):
    def threeConsecutiveOdds(self, arr):
        if len(arr) in [1, 2]:
            return False
        else:
            for i in range(len(arr) - 2):
                if arr[i] % 2 == 1 and arr[i + 1] % 2 == 1 and arr[i + 2] % 2 == 1:
                    return True
                else:
                    pass
        return False