class Solution(object):
    def climbStairs(self, n):
        hashmap = {}
        count = [0]
        def recur(val):
            if val in hashmap:
                count[0] += hashmap[val]
                return hashmap[val]
            else:
                if val > n:
                    hashmap[val] = 0
                    return 0
                elif (val == n):
                    count[0] += 1
                    hashmap[val] = 1
                    return 1
                else:
                    p1 = recur(val + 1)
                    p2 = recur(val + 2)
                    hashmap[val] = p1 + p2
                    return p1 + p2
        recur(0)
        return count[0]
          