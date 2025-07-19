class Solution(object):
    def isPrime(self, num):
        if num == 0 or num == 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    def countPrimeSetBits(self, left, right):
        ct = 0
        for i in range(left, right + 1):
            bin_i = bin(i).count('1')
            if Solution.isPrime(self, bin_i):
                ct += 1
        return ct
        