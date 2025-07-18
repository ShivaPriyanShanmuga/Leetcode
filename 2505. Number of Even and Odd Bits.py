class Solution(object):
    def evenOddBit(self, n):
        even = 0
        odd = 0
        bin_n = bin(n)[2:][::-1]
        for i in range(len(bin_n)):
            if bin_n[i] == '1':
                if i % 2 == 0:
                    even += 1
                else:
                    odd += 1
        return [even, odd]
        