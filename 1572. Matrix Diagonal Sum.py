class Solution(object):
    def diagonalSum(self, mat):
        l = len(mat)
        s = 0
        ind_l = 0
        while ind_l < l:
            s += mat[ind_l][ind_l]
            ind_l += 1
        mat_next = 0
        arr_next = len(mat[0]) - 1
        if l % 2 == 0:
            while mat_next < len(mat[0]):
                s += mat[mat_next][arr_next]
                mat_next += 1
                arr_next -= 1
        else:
            while mat_next < len(mat[0]):
                if mat_next != arr_next:
                    s += mat[mat_next][arr_next]
                mat_next += 1
                arr_next -= 1
        return s