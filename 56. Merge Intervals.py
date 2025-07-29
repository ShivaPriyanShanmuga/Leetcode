class Solution(object):
    def sortify(self, intervals):
        l = []
        for i in intervals:
            if l == []:
                l.append(i)
            else:
                ctr = 0
                while i[0] > l[ctr][0]:
                    if ctr < len(l):
                        ctr += 1
                        if ctr == len(l):
                            l.append(i)
                            break
                    else:
                        break
                if ctr < len(l):
                    l.insert(ctr, i)
                else:
                    l.append(i)
        return l
    def merger(self, inter, fin):
        if inter[1] >= fin[0]:
            return [[min(inter[0], fin[0]), max(inter[1], fin[1])]]
        else:
            return [inter, fin]
    def merge(self, intervals):
        a = []
        inter = [0, 0]
        intervals = Solution.sortify(self, intervals)
        ovfir = True
        while intervals != []:
            fir = intervals[0]
            if ovfir == True:
                ovfir = fir
            intervals.pop(0)
            merged = Solution.merger(self, inter, fir)
            if len(merged) == 2:
                a.append(merged[0])
                inter = merged[1]
            else:
                inter = merged[0]
        a.append(inter)
        if a[0] == [0, 0] and ovfir != [0, 0]:
            a.pop(0)
            return a
        else:
            return a
        