class Solution(object):
    def thousandSeparator(self, n):
        s = ''
        while n > 1000:
            x = str(n % 1000)
            x = '0' * (3 - len(x)) + x
            s = x + s
            n //= 1000
            s = '.' + s
        s = str(n) + s
        return s