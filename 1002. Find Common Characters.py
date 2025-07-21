class Solution(object):
    def commonChars(self, words):
        hashmap = {}
        for i in words[0]:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        for i in words:
            tmp_map = {}
            for j in i:
                if j in tmp_map:
                    tmp_map[j] += 1
                else:
                    tmp_map[j] = 1
            new_map = {}
            for j in hashmap:
                if j in tmp_map:
                    if hashmap[j] == tmp_map[j]:
                        new_map[j] = hashmap[j]
                    else:
                        new_map[j] = min(hashmap[j], tmp_map[j])
                else:
                    pass
            hashmap = new_map
        l = []
        for i in hashmap:
            l.extend(list(i * hashmap[i]))
        return l