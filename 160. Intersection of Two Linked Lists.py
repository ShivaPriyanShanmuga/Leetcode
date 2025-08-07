# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        hashmap = {}
        while headA:
            hashmap[headA] = ''
            headA = headA.next
        while headB:
            if headB in hashmap:
                return headB
            else:
                headB = headB.next
        return None