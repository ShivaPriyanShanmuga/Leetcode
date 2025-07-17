class Solution(object):
    def romanToInt(self, s):
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        sub_d = {'I':'VX', 'X':'LC', 'C':'DM'}
        sum = 0
        ind = 0
        while ind < len(s):
            if ind != len(s) - 1:
                if s[ind] in sub_d:
                    if s[ind + 1] in sub_d[s[ind]]:
                        sum = sum - d[s[ind]] + d[s[ind + 1]]
                        ind += 2
                    else:
                        sum += d[s[ind]]
                        ind += 1
                else:
                    sum += d[s[ind]]
                    ind += 1
            else:
                sum += d[s[ind]]
                ind += 1
        return sum