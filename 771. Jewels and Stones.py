class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        ct = 0
        for i in stones:
            if i in jewels:
                ct += 1
            else:
                pass
        return ct
        