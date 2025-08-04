class Solution(object):
    def wordPattern(self, pattern, s):
        s = s.split()
        if len(pattern) == len(s):
            hashmap = {}
            l = []
            for i in range(len(pattern)):
                if pattern[i] in hashmap:
                    if hashmap[pattern[i]] != s[i]:
                        return False
                elif pattern[i] not in hashmap:
                    if s[i] in l:
                        return False
                    else:
                        hashmap[pattern[i]] = s[i]
                        l.append(s[i])
            return True
        else:
            return False