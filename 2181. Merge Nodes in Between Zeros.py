# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeNodes(self, head):
        res = None
        sum = 0
        head = head.next
        while head:
            if head.val == 0:
                res = ListNode(sum, res)
                head = head.next
                sum = 0
            else:
                sum += head.val
                head = head.next
        final = None
        while res:
            final = ListNode(res.val, final)
            res = res.next
        return final