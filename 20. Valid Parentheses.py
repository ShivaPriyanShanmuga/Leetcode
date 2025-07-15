class Solution(object):
    def isValid(self, s):
        opening = '({['
        closing = ')}]'
        hashmap = {'(':')', '{':'}', '[':']'}
        stack = []
        for i in s:
            if i in opening:
                stack.append(i)
            else:
                if stack == []:
                    return False
                elif hashmap[stack[-1]] == i:
                    stack.pop()
                else:
                    return False
        return stack == []
        