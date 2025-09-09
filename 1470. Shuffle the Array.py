class Solution(object):
    def shuffle(self, nums, n):
        a1 = nums[:n]
        a2 = nums[n:]
        fin = []
        for i in range(n):
            fin.extend([a1[i], a2[i]])
        return fin