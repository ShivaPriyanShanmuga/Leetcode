class Solution(object):
    def numDifferentIntegers(self, word):
        modified = ''
        for i in word:
            if i.isalpha():
                modified += ' '
            else:
                modified += i
        l = modified.split()
        acc = []
        ct = 0
        for i in l:
            if int(i) not in acc:
                ct += 1
                acc.append(int(i))
        return ct