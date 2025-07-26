class Solution(object):
    def spacerem(self, s):
        while len(s) >= 1 and s[0] == ' ':
            s = s[1:]
        return s
    def myAtoi(self, s):
        sint = 0
        sprem = Solution.spacerem(self, s)
        if sprem == '':
            return sint
        else:
            signed = 0
            arr = "1234567890"
            if sprem[0] in arr:
                signed = '+'
            elif sprem[0] == '-':
                signed = '-'
                sprem = sprem[1:]
            elif sprem[0] == '+':
                signed = '+'
                sprem = sprem[1:]
            for i in sprem:
                if i in arr:
                    sint = sint * 10 + int(i)
                else:
                    break
            if sint > (2 ** 31) - 1 and signed == '+':
                return (2 ** 31) - 1
            elif sint > (2 ** 31) and signed == '-':
                return -(2 ** 31)
            elif signed == '-':
                return -(sint)
            else:
                return sint
            