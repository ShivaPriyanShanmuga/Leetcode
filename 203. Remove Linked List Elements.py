# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        if head == None:
            return None
        elif head.val == val:
            return Solution.removeElements(self, head.next, val)
        else:
            return ListNode(head.val, Solution.removeElements(self, head.next, val))