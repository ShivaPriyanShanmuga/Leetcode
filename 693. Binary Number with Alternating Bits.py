class Solution(object):
    def hasAlternatingBits(self, n):
        bin_n = bin(n)[2:]
        stack = []
        for i in bin_n:
            if stack == []:
                stack.append(i)
            elif stack[0] != i:
                stack.pop()
                stack.append(i)
            else:
                return False
        return True
        