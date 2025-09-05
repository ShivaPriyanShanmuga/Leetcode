class Solution(object):
    def uniqueOccurrences(self, arr):
        hashmap = {}
        for i in arr:
            if i in hashmap:
                pass
            else:
                hashmap[i] = arr.count(i)
        for i in hashmap:
            ct = hashmap[i]
            hashmap[i] = 0
            for j in hashmap:
                if hashmap[j] == ct:
                    return False
                else:
                    pass
        return True
        