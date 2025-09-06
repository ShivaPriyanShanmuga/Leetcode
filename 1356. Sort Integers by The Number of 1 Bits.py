class Solution(object):
    def sortByBits(self, arr):
        l = []
        h = {}
        for i in arr:
            n = bin(i).count('1')
            if n in h:
                h[n].append(i)
            else:
                h[n] = [i]
                l.append(n)
        l.sort(reverse=True)
        fin = []
        while l != []:
            h[l[-1]].sort()
            fin.extend(h[l[-1]])
            l.pop()
        return fin