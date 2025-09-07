class Solution(object):
    def reformat(self, s):
        la = []
        ld = []
        for i in s:
            if i.isalpha():
                la.append(i)
            else:
                ld.append(i)
        fin = ''
        if len(la) == len(ld):
            for i in range(len(la)):
                fin += la[i] + ld[i]
        elif len(la) - len(ld) == 1:
            for i in range(len(ld)):
                fin += la[i] + ld[i]
            fin += la[-1]
        elif len(ld) - len(la) == 1:
            for i in range(len(la)):
                fin += la[i] + ld[i]
            fin = ld[-1] + fin
        return fin