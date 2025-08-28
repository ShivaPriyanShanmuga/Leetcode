class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        arr = []
        ans = []
        for i in arr1:
            if i not in arr2:
                arr.append(i)
            else:
                pass
        arr.sort()
        for i in arr2:
            while i in arr1:
                ans.append(i)
                arr1.remove(i)
        ans.extend(arr)
        return ans
        