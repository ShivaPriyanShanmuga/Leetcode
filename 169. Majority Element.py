class Solution(object):
    def majorityElement(self, nums):
        hashmap = {}
        l = len(nums) // 2
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        for i in hashmap:
            if hashmap[i] > l:
                return i
            else:
                pass