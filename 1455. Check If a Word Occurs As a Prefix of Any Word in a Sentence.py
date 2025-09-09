class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        sentence = sentence.split()
        for i in range(len(sentence)):
            if sentence[i].startswith(searchWord):
                return i + 1
            else:
                pass
        return -1
        