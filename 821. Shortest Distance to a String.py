class Solution(object):
    def shortestToChar(self, s, c):
        answer = []
        ind_arr = []
        for i in range(len(s)):
            if s[i] == c:
                ind_arr.append(i)
        def mini(ind):
            mini = 10000
            for i in ind_arr:
                if abs(ind - i) < mini:
                    mini = abs(ind - i)
            return mini
        for i in range(len(s)):
            if s[i] == c:
                answer.append(0)
            else:
                answer.append(mini(i))
        return answer
    