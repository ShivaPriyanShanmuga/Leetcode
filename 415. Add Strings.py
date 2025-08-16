class Solution(object):
    def help(self, num1, num2):
        if num1 == '':
            return "1"
        else:
            if int(num1[0]) + 1 >= 10:
                return str(int(num1[0]) - 9) + Solution.help(self, num1[1:], '1')
            else:
                return str(int(num1[0]) + 1) + num1[1:]

    def addStrings(self, num1, num2):
        num1 = num1[::-1]
        num2 = num2[::-1]
        res = ''
        while num1 and num2:
            if int(num1[0]) + int(num2[0]) >= 10:
                res += str(int(num1[0]) + int(num2[0]) - 10)
                num1  = Solution.help(self, num1[1:], "1")
                num2 = num2[1:]
            else:
                res += str(int(num1[0]) + int(num2[0]))
                num1 = num1[1:]
                num2 = num2[1:]
        if num1 == '' and num2 == '':
            return res[::-1]
        elif num1 == '':
            return (res + num2)[::-1]
        elif num2 == '':
            return (res + num1)[::-1]