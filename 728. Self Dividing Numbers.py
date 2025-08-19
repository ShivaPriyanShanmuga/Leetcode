class Solution(object):
    def selfDividingNumbers(self, left, right):
        arr = []
        for i in range(left, right + 1):
            s = str(i)
            t = True
            for j in s:
                if j == '0':
                    t = False
                    break
                elif i % int(j) == 0:
                    pass
                else:
                    t = False
                    break
            if t:
                arr.append(i)
            else:
                pass
        return arr