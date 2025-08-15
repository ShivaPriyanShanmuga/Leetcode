class Solution(object):
    def topKFrequent(self, nums, k):
        acc = []
        dict = {}
        for i in nums:
            if i not in dict:
                dict[i] = nums.count(i)
            else:
                pass
        
        for j in range(k):
            max = (0, 0)
            for i in dict:
                if dict[i] > max[-1]:
                    max = (i, dict[i])
                else:
                    pass
            acc.append(max[0])
            dict.pop(max[0])
        return acc