class Solution(object):
    def setZeroes(self, matrix):
        rows = []
        columns = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    if i not in rows:
                        rows.append(i)
                    if j not in columns:
                        columns.append(j)
        for j in range(len(matrix)):
            if j not in rows:
                for i in columns:
                    matrix[j][i] = 0
            else:
                matrix[j] = [0] * len(matrix[0])