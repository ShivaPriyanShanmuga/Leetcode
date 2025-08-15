class Solution(object):
    def intersect(self, nums1, nums2):
        h = {}
        l = min(len(nums2), len(nums1))
        if l == len(nums2):
            for i in nums2:
                if i in h:
                    pass
                else:
                    h[i] = min(nums1.count(i), nums2.count(i))
        else:
            for i in nums1:
                if i in h:
                    pass
                else:
                    h[i] = min(nums1.count(i), nums2.count(i))
        arr = []
        for i in h:
            while h[i] != 0:
                arr.append(i)
                h[i] -= 1
        return arr
            