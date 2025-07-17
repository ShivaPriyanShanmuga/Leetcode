class Solution(object):
    def hammingDistance(self, x, y):
        hamming_distance = 0
        x_bin = bin(x)[2:]
        y_bin = bin(y)[2:]
        if len(x_bin) > len(y_bin):
            y_bin = '0' * (len(x_bin) - len(y_bin)) + y_bin
        elif len(y_bin) > len(x_bin):
            x_bin = '0' * (len(y_bin) - len(x_bin)) + x_bin
        for i in range(len(x_bin)):
            if x_bin[i] == y_bin[i]:
                pass
            else:
                hamming_distance += 1
        return hamming_distance