class Solution(object):
    def findShortestSubArray(self, nums):
        hashmap = {}
        max_ = 0
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
                if hashmap[i] > max_:
                    max_ = hashmap[i]
            else:
                hashmap[i] = 1
                if hashmap[i] > max_:
                    max_ = hashmap[i]
        l = []
        for i in hashmap:
            if hashmap[i] == max_:
                l.append(i)
            else:
                pass
        rev = nums[::-1]
        leng = []
        for i in l:
            ind1 = nums.index(i)
            ind2 = len(nums) - rev.index(i)
            leng.append(ind2 - ind1)
        return min(leng)
