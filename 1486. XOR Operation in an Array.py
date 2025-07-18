class Solution(object):
    def xorOperation(self, n, start):
        nums = [start + 2 * i for i in range(n)]
        res = 0
        ind = 0
        while ind < n:
            if n == 1:
                res = nums[0]
                ind += 1
            else:
                res = res ^ nums[ind]
                ind += 1
        return res
        