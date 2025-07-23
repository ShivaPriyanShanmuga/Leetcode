class Solution(object):
    def countWords(self, words1, words2):
        hashmap = {}
        ct = 0
        for i in words1:
            if i in hashmap:
                hashmap[i][0] += 1
            else:
                hashmap[i] = [1, 0]
        for i in words2:
            if i in hashmap:
                hashmap[i][1] += 1
            else:
                pass
        for i in hashmap:
            if hashmap[i] == [1, 1]:
                ct += 1
        return ct