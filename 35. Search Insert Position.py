class Solution(object):
    def searchInsert(self, nums, target):
        if len(nums) == 1:
            if nums[0] < target:
                return 1
            else:
                return 0
        elif nums[0] >= target:
            return 0
        elif target > nums[0]:
            arr1 = nums[:len(nums) // 2]
            arr2 = nums[len(nums) // 2:]
            if nums[(len(nums) // 2) - 1] >= target:
                return Solution.searchInsert(self, arr1, target)
            else:
                return (len(nums) // 2) + Solution.searchInsert(self, arr2, target)