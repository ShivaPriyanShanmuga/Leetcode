class Solution(object):
    def minChanges(self, n, k):
        ct = 0
        bin_n = bin(n)[2:]
        bin_k = bin(k)[2:]
        if len(bin_k) > len(bin_n):
            return -1
        elif len(bin_k) < len(bin_n):
            bin_k = '0' * (len(bin_n) - len(bin_k)) + bin_k
        for i in range(len(bin_n)):
            if bin_n[i] == '0':
                if bin_k[i] == '0':
                    pass
                else:
                    return -1
            else:
                if bin_k[i] == '1':
                    pass
                else:
                    ct += 1
        return ct