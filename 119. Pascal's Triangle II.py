class Solution(object):
    def help(self, prev):
        new = []
        for i in range(len(prev)):
            if i == len(prev) - 1:
                pass
            else:
                new.append(prev[i] + prev[i + 1])
        new.insert(0, 1)
        new.append(1)
        return new
    def getRow(self, rowIndex):
        arr = []
        prev = [1, 1]
        while rowIndex != -1:
            if rowIndex == 0:
                arr.insert(0, [1])
                rowIndex -= 1
            elif rowIndex == 1:
                arr.insert(0, [1, 1])
                rowIndex -= 1
            else:
                prev = Solution.help(self, prev)
                arr.append(prev)
                rowIndex -= 1
        return arr[::-1][0]
        