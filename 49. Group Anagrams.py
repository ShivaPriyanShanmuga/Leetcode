class Solution(object):
    def groupAnagrams(self, strs):
        d = {}
        for i in strs:
            swrd = "".join(sorted(i))
            if swrd in d.keys():
                d[swrd].append(i)
            else:
                d[swrd] = [i]
        return list(d.values())