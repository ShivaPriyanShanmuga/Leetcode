class Solution(object):
    def sortString(self, s):
        hashmap = {}
        for i in s:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        result = ''
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        rev = alpha[::-1]
        while hashmap != {}:
            for i in alpha:
                if i in hashmap:
                    if hashmap[i] != 1:
                        hashmap[i] -= 1
                    else:
                        hashmap.pop(i)
                    result += i
                else:
                    pass
            for i in rev:
                if i in hashmap:
                    if hashmap[i] != 1:
                        hashmap[i] -= 1
                    else:
                        hashmap.pop(i)
                    result += i
                else:
                    pass
        return result