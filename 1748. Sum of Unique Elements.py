class Solution(object):
    def sumOfUnique(self, nums):
        sum = 0
        hashmap = {}
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        for i in hashmap:
            if hashmap[i] == 1:
                sum += i
        return sum