class Solution(object):
    def checkIfPangram(self, sentence):
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        for i in alpha:
            if i not in sentence:
                return False
        return True