class Solution(object):
    def findWords(self, words):
        result = []
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        for i in words:
            l = ''
            for j in i:
                if j not in l:
                    l += j.lower()
            if l[0] in row1:
                condi = True
                for j in l:
                    if j not in row1:
                        condi = False
                        break
                if condi:
                    result.append(i)
            elif l[0] in row2:
                condi = True
                for j in l:
                    if j not in row2:
                        condi = False
                        break
                if condi:
                    result.append(i)
            elif l[0] in row3:
                condi = True
                for j in l:
                    if j not in row3:
                        condi = False
                        break
                if condi:
                    result.append(i)

        return result