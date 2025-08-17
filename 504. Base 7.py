class Solution(object):
    def log(self, num):
        ct = 0
        while num >= 7:
            ct += 1
            num /= 7
        return ct
    def convertToBase7(self, num):
        loga = Solution.log(self, num)
        if num >= 0:
            fin = ""
            while loga > -1:
                res = num // (7 ** loga)
                fin += str(res)
                num -= res * (7 ** loga)
                loga -= 1
            return fin
        else:
            return "-" + Solution.convertToBase7(self, -(num))