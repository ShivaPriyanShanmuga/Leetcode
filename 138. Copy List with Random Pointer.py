# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        tmp1 = head
        l = []
        hashmap = {}
        ind = 0
        while tmp1:
            hashmap[tmp1] = ind
            tmp1 = tmp1.next
            ind += 1
        def copy(lst):
            if lst:
                return Node(lst.val, copy(lst.next))
            else:
                return None
        cpy = copy(head)
        tmp2 = cpy
        l = []
        while tmp2:
            l.append(tmp2)
            tmp2 = tmp2.next
        tmp3 = cpy
        while head:
            if head.random == None:
                tmp3.random = None
            else:
                tmp3.random = l[hashmap[head.random]]
            tmp3 = tmp3.next
            head = head.next
        return cpy