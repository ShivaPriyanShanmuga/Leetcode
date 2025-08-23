class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        if len(nums) - k > k:
            while k:
                k -= 1
                nums.insert(0, nums.pop())
        else:
            val = len(nums) - k
            while val:
                val -= 1
                nums.append(nums.pop(0))