class Solution(object):
    def kthDistinct(self, arr, k):
        ans = []
        for i in arr:
            if len(ans) == k:
                break
            elif arr.count(i) == 1:
                ans.append(i)
        if len(ans) < k:
            return ""
        else:
            return ans[k - 1]