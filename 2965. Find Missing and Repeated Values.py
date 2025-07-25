class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        n = len(grid)
        hashmap = {}
        for i in grid:
            for j in i:
                if j in hashmap:
                    hashmap[j] += 1
                else:
                    hashmap[j] = 1
        a = None
        b = None
        for i in range(1, (n ** 2) + 1):
            if i not in hashmap:
                b = i
            elif hashmap[i] == 2:
                a = i
        return [a, b]