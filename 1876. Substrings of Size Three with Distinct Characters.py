class Solution(object):
    def countGoodSubstrings(self, s):
        if len(s) < 3:
            return 0
        else:
            ct = 0
            ind = 0
            while ind < len(s) - 2:
                substring = s[ind : ind+3]
                modified = ''
                for i in substring:
                    if i not in modified:
                        modified += i
                if len(modified) == 3:
                    ct += 1
                ind += 1
            return ct