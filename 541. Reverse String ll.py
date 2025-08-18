class Solution(object):
    def reverseStr(self, s, k):
        ans = ''
        while s != '':
            ans += s[:k][::-1]
            ans += s[k:2*k]
            s = s[2*k:]
        return ans