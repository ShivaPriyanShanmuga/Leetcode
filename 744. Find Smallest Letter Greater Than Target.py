class Solution(object):
    def nextGreatestLetter(self, letters, target):
        for i in letters:
            if i > target:
                return i
            else:
                pass
        return letters[0]
        