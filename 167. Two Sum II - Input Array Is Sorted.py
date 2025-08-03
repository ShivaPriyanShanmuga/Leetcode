class Solution(object):
    def twoSum(self, numbers, target):
        arr = []
        low = -1000 + target
        high = 1000
        while -2000 <= low <= 2000 and -2000 <= high <= 2000:
            if low in numbers and high in numbers:
                min = numbers.index(low) + 1
                numbers[numbers.index(low)] = -100000
                return [min, numbers.index(high) + 1]
            else:
                low += 1
                high -= 1