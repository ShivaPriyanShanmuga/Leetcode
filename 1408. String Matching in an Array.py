class Solution(object):
    def stringMatching(self, words):
        acc = []
        for i in words:
            for j in words:
                if i in j and i != j and i not in acc:
                    acc.append(i)
        return acc
        