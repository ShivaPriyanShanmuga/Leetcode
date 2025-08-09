class Solution(object):
    def majorityElement(self, nums):
        hashmap = {}
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        arr = []
        l = len(nums) // 3
        for i in hashmap:
            if hashmap[i] > l:
                arr.append(i)
            else:
                pass
        return arr