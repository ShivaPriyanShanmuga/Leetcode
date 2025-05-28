class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums1.extend(nums2)
        nums1.sort()
        l = nums1
        if len(l) % 2 == 0:
            return float(l[len(l)/2 - 1] + l[len(l)/2]) / 2
        else:
            return l[len(l)/2]
