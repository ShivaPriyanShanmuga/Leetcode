class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n = bin(n)[2:]
        n = '0' * (32 - len(n)) + n
        s = '0b' + n[::-1]
        return int(s, 2)