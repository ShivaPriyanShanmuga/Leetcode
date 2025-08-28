class Solution(object):
    def bitwiseComplement(self, n):
        bi = bin(n)[2:]
        ans = '0b'
        for i in bi:
            if i == '1':
                ans += '0'
            else:
                ans += '1'
        return int(ans, 2)
        