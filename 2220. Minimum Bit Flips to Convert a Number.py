class Solution(object):
    def minBitFlips(self, start, goal):
        num = 0
        start_bin = bin(start)[2:]
        goal_bin = bin(goal)[2:]
        if len(start_bin) > len(goal_bin):
            goal_bin = '0' * (len(start_bin) - len(goal_bin)) + goal_bin
        elif len(start_bin) < len(goal_bin):
            start_bin = '0' * (len(goal_bin) - len(start_bin)) + start_bin
        for i in range(len(goal_bin)):
            if start_bin[i] != goal_bin[i]:
                num += 1
        return num