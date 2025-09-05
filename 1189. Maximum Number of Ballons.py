class Solution(object):
    def maxNumberOfBalloons(self, text):
        hashmap = {'b':0, 'a':0, 'l':0, 'o':0, 'n':0}
        arr = []
        for i in text:
            if i in hashmap:
                hashmap[i] += 1
            else:
                pass
        for i in hashmap:
            if i == 'l' or i == 'o':
                arr.append(hashmap[i] // 2)
            else:
                arr.append(hashmap[i])
        return min(arr)