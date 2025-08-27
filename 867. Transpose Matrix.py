class Solution(object):
    def transpose(self, matrix):
        res = []
        for i in range(len(matrix[0])):
            res.append([0] * len(matrix))
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                res[j][i] = matrix[i][j]
        return res
        