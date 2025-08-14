class Solution(object):
    def reverseVowels(self, s):
        v = 'aAeEiIoOuU'
        a = list(s)
        arr = []
        ans = ''
        for i in s:
            if i in v:
                arr.append(i)
            else:
                pass
        arr = arr[::-1]
        for i in s:
            if i in v:
                ans = ans + arr.pop(0)
            else:
                ans = ans + i
        return ans