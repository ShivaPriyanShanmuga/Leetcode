class Solution(object):
    def areOccurrencesEqual(self, s):
        hashmap = {}
        for i in s:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        l = []
        for i in hashmap:
            if hashmap[i] not in l:
                l.append(hashmap[i])
        return len(l) == 1