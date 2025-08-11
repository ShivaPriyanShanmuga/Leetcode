class Solution(object):
    def isAnagram(self, s, t):
        for i in s:
            if t.count(i) == s.count(i):
                pass
            else:
                return False
        for i in t:
            if t.count(i) == s.count(i):
                pass
            else:
                return False
        return True
