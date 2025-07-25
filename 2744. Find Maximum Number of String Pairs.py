class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        l = []
        ct = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[i] not in l and words[j] not in l and words[i] == words[j][::-1]:
                    l.append(words[i])
                    l.append(words[j])
                    ct += 1
        return ct