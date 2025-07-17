class Solution(object):
    def flip(self, lst):
        for i in range(len(lst)):
            if lst[i] == 1:
                lst[i] = 0
            else:
                lst[i] = 1
        return lst
    def flipAndInvertImage(self, image):
        res = []
        for i in image:
            res.append(Solution.flip(self, i[::-1]))
        return res