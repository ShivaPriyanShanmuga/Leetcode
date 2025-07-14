class Solution(object):
    def replaceWords(self, dictionary, sentence):
        l = sentence.split()
        for i in range(len(l)):
            for j in dictionary:
                if l[i].startswith(j):
                    l[i] = j
        return " ".join(l)