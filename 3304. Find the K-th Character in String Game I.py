class Solution(object):
    def kthCharacter(self, k):
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        word = 'a'
        while len(word) < k:
            new_word = ''
            for i in range(len(word)):
                new_word += alphabets[(alphabets.index(word[i]) + 1)% 26]
            word += new_word
        return word[k - 1]