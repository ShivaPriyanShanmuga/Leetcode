class Solution(object):
    def subsets(self, nums):
        ans = []
        subset = []
        def solve(i):
            if i > len(nums) - 1:
                ans.append(subset[:])
                return
            subset.append(nums[i])
            solve(i + 1)
            subset.pop()
            solve(i + 1)
        solve(0)
        return ans