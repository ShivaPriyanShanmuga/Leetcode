class Solution(object):
    def numberOfSteps(self, num):
        ct = 0
        while num != 1:
            if num == 0:
                return 0
            elif num % 2 == 0:
                num /= 2
                ct += 1
            else:
                num -= 1
                ct += 1
        return ct + 1