class Solution(object):
    def destCity(self, paths):
        hashmap = {}
        for i in paths:
            hashmap[i[0]] = i[1]
        cur = paths[0][0]
        while cur in hashmap:
            cur = hashmap[cur]
        return cur