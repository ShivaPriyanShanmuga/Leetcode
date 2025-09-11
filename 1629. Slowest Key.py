class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        d = []
        d.append(releaseTimes[0])
        for i in range(1, len(releaseTimes)):
            d.append(releaseTimes[i] - releaseTimes[i - 1])
        m = max(d)
        j = []
        for i in range(len(d)):
            if d[i] == m:
                j.append(keysPressed[i])
            else:
                pass
        return max(j)