class Solution(object):
    def minimumOperations(self, nums):
        l = []
        for i in nums:
            if i != 0:
                l.append(i)
        nums = l[:]
        ct = 0
        while nums != []:
            mini = min(nums)
            for i in range(len(nums)):
                nums[i] -= mini
            ct += 1
            l = []
            for i in nums:
                if i != 0:
                    l.append(i)
            nums = l[:]
        return ct