class Solution(object):
    def form(self, comp ,master):
        new = ""
        for i in range(min(len(comp), len(master))):
            if comp[i] == master[i]:
                new += comp[i]
            else:
                break
        return new
    def longestCommonPrefix(self, strs):
        common = strs[0]
        for i in strs:
            common = Solution.form(self, i, common)
        return common