class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        ct = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                ct += 1
            else:
                pass
        return ct
        