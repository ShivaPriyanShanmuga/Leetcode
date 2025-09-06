class Solution(object):
    def maximum69Number (self, num):
        arr = []
        for i in str(num):
            arr.append(i)
        for i in range(len(arr)):
            if arr[i] == '6':
                arr[i] = '9'
                break
            else:
                pass
        return int(''.join(arr))