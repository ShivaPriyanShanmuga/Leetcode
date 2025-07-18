class Solution(object):
    def decode(self, encoded, first):
        actual = []
        ptr = first
        for i in encoded:
            actual.append(ptr ^ i)
            ptr = actual[-1]
        actual = [first] + actual
        return actual
        