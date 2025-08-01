class Solution(object):
    def isPalindrome(self, s):
        string = ''
        for i in s:
            if i.isalnum():
                string += i
            else:
                pass
        string = string.lower()
        return string == string[::-1]