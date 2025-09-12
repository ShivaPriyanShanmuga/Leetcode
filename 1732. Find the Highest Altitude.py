class Solution(object):
    def largestAltitude(self, gain):
        act = [0]
        prev = 0
        for i in gain:
            prev += i
            act.append(prev)
        return max(act)