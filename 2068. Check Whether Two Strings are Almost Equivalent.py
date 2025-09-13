class Solution(object):
    def checkAlmostEquivalent(self, word1, word2):
        hashmap = {}
        for i in word1:
            if i in hashmap:
                hashmap[i][0] += 1
            else:
                hashmap[i] = [1, 0]
        for i in word2:
            if i in hashmap:
                hashmap[i][1] += 1
            else:
                hashmap[i] = [0, 1]
        for i in hashmap:
            if abs(hashmap[i][1] - hashmap[i][0]) > 3:
                return False
        return True
        