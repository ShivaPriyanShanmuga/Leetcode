class Solution(object):
    def binaryGap(self, n):
        dist = []
        indices = []
        bin_n = bin(n)
        for i in range(len(bin_n)):
            if bin_n[i] == '1':
                indices.append(i)
        if len(indices) == 1:
            return 0
        else:
            for i in range(len(indices) - 1):
                dist.append(indices[i + 1] - indices[i])
        return max(dist)