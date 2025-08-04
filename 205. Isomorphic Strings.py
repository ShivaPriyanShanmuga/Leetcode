class Solution(object):
    def isIsomorphic(self, s, t):
        hashmap = {}
        for i in range(len(s)):
            if s[i] in hashmap:
                if hashmap[s[i]] == t[i]:
                    pass
                else:
                    return False
            else:
                hashmap[s[i]] = t[i]
        l = []
        for i in hashmap:
            if hashmap[i] in l:
                return False
            else:
                l.append(hashmap[i])
        return True