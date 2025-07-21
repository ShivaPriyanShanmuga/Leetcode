class Solution(object):
    def minOperations(self, nums, k):
        l = set([i + 1 for i in range(k)])
        collection = []
        ct = 0
        while set(collection) != l:
            elem = nums.pop()
            if elem in l:
                collection.append(elem)
            ct += 1
        return ct