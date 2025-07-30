class Solution(object):
    def plusOne(self, digits):
        l = digits[::-1]
        if l == []:
            return [1]
        elif l[0] == 9:
            s = (Solution.plusOne(self, l[:0:-1]))
            s.append(0)
            return s
        else:
            l[0] += 1
            return l[::-1]
        