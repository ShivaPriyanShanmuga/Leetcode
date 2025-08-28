class Solution(object):
    def prefixesDivBy5(self, nums):
        s = '0b'
        a = []
        for i in nums:
            s += str(i)
            s = int(s, 2)
            if s % 5 == 0:
                a.append(True)
                s = bin(s)
            else:
                a.append(False)
                s = bin(s)
        return a
            
        for i in range(len(a)):
            a[i] = int(a[i], 2)
        fin = []
        for i in a:
            if i % 5 == 0:
                fin.append(True)
            else:
                fin.append(False)
        return fin