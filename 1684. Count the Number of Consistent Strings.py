class Solution(object):
    def countConsistentStrings(self, allowed, words):
        ct = 0
        for i in words:
            for j in i:
                if j in allowed:
                    pass
                else:
                    break
            else:
                ct += 1
        return ct
        