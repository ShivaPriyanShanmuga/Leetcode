class Solution(object):
    def minimizedStringLength(self, s):
        result = ''
        for i in s[::-1]:
            if i not in result:
                result = i + result
        return len(result)