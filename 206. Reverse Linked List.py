# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        h = None
        while head != None:
            h = ListNode(head.val, h)
            head = head.next
        return h