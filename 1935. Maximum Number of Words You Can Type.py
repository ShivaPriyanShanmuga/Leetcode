class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        ct = 0
        text = text.split()
        for i in text:
            cond = True
            for j in i:
                if j in brokenLetters:
                    cond = False
                    break
            if cond:
                ct += 1
        return ct