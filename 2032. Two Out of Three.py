class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        set1 = set(nums1)&set(nums2)
        set2 = set(nums2)&set(nums3)
        set3 = set(nums3)&set(nums1)
        return list(set1|set2|set3)