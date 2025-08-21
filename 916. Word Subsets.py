class Solution(object):
    def wordSubsets(self, words1, words2):
        arr = []
        d = {}
        for j in words2:
            for k in j:
                if k in d:
                    if d[k] < j.count(k):
                        d[k] = j.count(k)
                    else:
                        pass
                else:
                    d[k] = j.count(k)
        for i in words1:
            t = True
            for j in d:
                if d[j] <= i.count(j):
                    pass
                else:
                    t = False
                    break
            if t:
                arr.append(i)
            else:
                pass
        return arr                