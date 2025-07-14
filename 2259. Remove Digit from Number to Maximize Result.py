class Solution(object):
    def removeDigit(self, number, digit):
        l = []
        for i in range(len(number)):
            if number[i] == digit:
                l.append(int(number[:i] + number[i+1:]))
            else:
                pass
        return str(max(l))
        