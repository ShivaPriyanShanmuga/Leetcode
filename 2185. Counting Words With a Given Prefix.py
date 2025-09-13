class Solution(object):
    def prefixCount(self, words, pref):
        ct = 0
        for i in words:
            if pref == i[:len(pref)]:
                ct += 1
            else:
                pass
        return ct
        