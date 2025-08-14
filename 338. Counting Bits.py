class Solution(object):
    def countBits(self, n):
        ans = []
        for i in range(n + 1):
            i = bin(i)[2:]
            ans.append(i.count('1'))
        return ans