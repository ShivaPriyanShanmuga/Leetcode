class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        m = max(candies)
        a = []
        for i in candies:
            if i + extraCandies >= m:
                a.append(True)
            else:
                a.append(False)
        return a