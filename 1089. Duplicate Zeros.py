class Solution(object):
    def duplicateZeros(self, arr):
        ctr = 0
        l = len(arr)
        while ctr < l:
            if arr[ctr] == 0:
                arr.insert(ctr, 0)
                ctr += 2
                arr.pop()
            else:
                ctr += 1
        
        