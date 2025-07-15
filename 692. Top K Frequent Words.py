class Solution(object):
    def topKFrequent(self, words, k):
        h = {}
        for i in words:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
        m = max(h.values())
        nh = {}
        for i in range(int(m)):
            nh[i+1] = []
        for i in h:
            nh[h[i]].append(i)
        print(nh)
        for i in nh:
            nh[i].sort()
        print(nh)
        l = []
        while k > 0:
            if nh[max(nh)] == []:
                nh.pop(max(nh))
            elif len(nh[max(nh)]) > k:
                l.extend(nh[max(nh)][:k])
                k = 0
            else:
                l.extend(nh[max(nh)])
                k -= len(nh[max(nh)])
                nh.pop(max(nh))
        return l
        