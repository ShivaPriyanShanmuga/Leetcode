class Solution(object):
    def secondHighest(self, s):
        l = []
        for i in s:
            if i.isdigit() and int(i) not in l:
                l.append(int(i))
        if len(l) < 2:
            return -1
        l.sort()
        return l[-2]