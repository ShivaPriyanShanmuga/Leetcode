class Solution(object):
    def subsetXORSum(self, nums):
        arr = []
        subset = []
        def solve(i):
            if i > len(nums) - 1:
                arr.append(subset[:])
                return
            subset.append(nums[i])
            solve(i + 1)
            subset.pop()
            solve(i + 1)
        solve(0)
        sum = 0
        for i in arr:
            XOR_val = 0
            for j in i:
                XOR_val = XOR_val ^ j
            sum += XOR_val
        return sum