class Solution(object):
    def reverseWords(self, s):
        a = []
        st = s.split()
        for i in st:
            a.append(i[::-1])
        return " ".join(a)