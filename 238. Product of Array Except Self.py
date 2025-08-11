class Solution(object):
    def productExceptSelf(self, nums):
        pro = 1
        zin = 0
        for i in nums:
            if i != 0:
                pro *= i
            else:
                zin += 1
        ans = []
        if zin == 1:
            for i in nums:
                if i != 0:
                    ans.append(0)
                else:
                    ans.append(pro)
        elif zin > 1:
            for i in nums:
                ans.append(0)
        else:
            for i in nums:
                ans.append(pro // i)
        return ans
        