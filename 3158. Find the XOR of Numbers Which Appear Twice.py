class Solution(object):
    def duplicateNumbersXOR(self, nums):
        hashmap = {1:[], 2:[]}
        for i in nums:
            if i in hashmap[1]:
                hashmap[1].remove(i)
                hashmap[2].append(i)
            else:
                hashmap[1].append(i)
        result = 0
        for i in hashmap[2]:
            result = i ^ result
        return result