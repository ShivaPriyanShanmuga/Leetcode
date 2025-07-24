class Solution(object):
    def maxFreqSum(self, s):
        vowel = 'aeiou'
        alpha = "abcdefghijklmnopqrstuvwxyz"
        v_hashmap = {}
        c_hashmap = {}
        for i in alpha:
            if i not in vowel:
                c_hashmap[i] = 0
            else:
                v_hashmap[i] = 0
        for i in s:
            if i in vowel:
                v_hashmap[i] += 1
            else:
                c_hashmap[i] += 1
        return max(v_hashmap.values()) + max(c_hashmap.values())