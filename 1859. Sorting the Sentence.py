class Solution(object):
    def sortSentence(self, s):
        h = {}
        s = s.split()
        for i in s:
            ind = int(i[-1])
            h[ind] = str(i[:-1])
        fin = []
        l = h.keys()
        l.sort()
        for i in l:
            fin.append(h[i])
        return " ".join(fin)
        