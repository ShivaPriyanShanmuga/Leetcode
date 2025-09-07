class Solution(object):
    def sum(self, n):
        s = str(n)
        su = 0
        for i in s:
            su += int(i)
        return su
    def countLargestGroup(self, n):
        hashmap = {}
        for i in range(n):
            sumi = Solution.sum(self, i + 1)
            if sumi in hashmap:
                hashmap[sumi] += 1
            else:
                hashmap[sumi] = 1
        maxi = max(list(hashmap.values()))
        ct = 0
        for i in hashmap:
            if hashmap[i] == maxi:
                ct += 1
            else:
                pass
        return ct
        