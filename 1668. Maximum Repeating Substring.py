class Solution(object):
    def maxRepeating(self, sequence, word):
        m = 0
        ori = word
        while word in sequence:
            m += 1
            word = word + ori
        return m
        