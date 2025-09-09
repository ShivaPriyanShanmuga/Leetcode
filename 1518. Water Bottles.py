class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        ct = 0
        while numBottles >= numExchange:
            ct += (numBottles // numExchange) * numExchange
            numBottles = (numBottles % numExchange) + (numBottles // numExchange)
        ct += numBottles
        if numBottles == 0:
            return ct + 1
        return ct