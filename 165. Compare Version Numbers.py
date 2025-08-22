class Solution(object):
    def compareVersion(self, version1, version2):
        v1 = [int(i) for i in version1.split('.')]
        v2 = [int(i) for i in version2.split('.')]
        if len(v1) < len(v2):
            v1 += [0] * (len(v2) - len(v1))
        elif len(v2) < len(v1):
            v2 += [0] * (len(v1) - len(v2))
        for i in range(len(v1)):
            if v1[i] > v2[i]:
                return 1
            elif v2[i] > v1[i]:
                return -1
            else:
                pass
        return 0
