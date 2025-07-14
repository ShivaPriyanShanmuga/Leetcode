class Solution(object):
    def findRepeatedDnaSequences(self, s):
        if len(s) < 10:
            return []
        else:
            h = {}
            for i in range(len(s)):
                if len(s) - i < 10:
                    pass
                elif s[i:i+10] in h:
                    h[s[i:i+10]] += 1
                else:
                    h[s[i:i+10]] = 1
            l = []
            for i in h:
                if h[i] > 1:
                    l.append(i)
            return l
        