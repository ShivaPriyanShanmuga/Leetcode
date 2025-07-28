# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        if head == None:
            return None
        elif head.next == None:
            return head
        else:
            return ListNode(head.next.val, ListNode(head.val, Solution.swapPairs(self, head.next.next)))