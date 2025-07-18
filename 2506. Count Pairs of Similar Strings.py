class Solution(object):
    def checkSimilar(self, wrd1, wrd2):
        for i in wrd1:
            if i not in wrd2:
                return False
        for i in wrd2:
            if i not in wrd1:
                return False
        return True
    def similarPairs(self, words):
        ct = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if Solution.checkSimilar(self, words[i], words[j]):
                    ct += 1
        return ct
        