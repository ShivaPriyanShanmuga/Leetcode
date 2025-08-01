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
    def generate(self, numRows):
        arr = []
        prev = [1, 1]
        while numRows:
            if numRows == 1:
                arr.insert(0, [1])
                numRows -= 1
            elif numRows == 2:
                arr.insert(0, [1, 1])
                numRows -= 1
            else:
                prev = Solution.help(self, prev)
                arr.append(prev)
                numRows -= 1
        return arr
        