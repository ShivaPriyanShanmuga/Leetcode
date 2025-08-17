class Solution(object):
    def findComplement(self, num):
        s = bin(num)[2:]
        comp = '0b'
        for i in s:
            if i == '0':
                comp += '1'
            else:
                comp += '0'
        return int(comp, 2)