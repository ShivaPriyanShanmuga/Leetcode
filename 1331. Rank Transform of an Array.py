class Solution(object):
    def arrayRankTransform(self, arr):
        copy = arr[:]
        hashmap = {}
        copy.sort()
        cur = 1
        for i in copy:
            if i not in hashmap:
                hashmap[i] = cur
                cur += 1
        result = []
        for i in arr:
            result.append(hashmap[i])
        return result