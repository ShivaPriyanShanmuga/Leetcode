class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        l = s1.split() + s2.split()
        h = {}
        for i in l:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
        res = []
        for i in h:
            if h[i] == 1:
                res.append(i)
        
        return res