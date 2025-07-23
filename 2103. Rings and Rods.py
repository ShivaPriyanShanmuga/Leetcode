class Solution(object):
    def countPoints(self, rings):
        hashmap = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}
        ind = 0
        while ind < len(rings):
            if rings[ind] not in hashmap[int(rings[ind + 1])]:
                hashmap[int(rings[ind + 1])].append(rings[ind])
            ind += 2
        ct = 0
        for i in hashmap:
            if len(hashmap[i]) == 3:
                ct += 1
        return ct