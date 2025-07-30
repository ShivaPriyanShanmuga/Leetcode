# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def deleteDuplicates(self, head):
        if head == None:
            return None
        elif head.next == None:
            return head
        elif head.val == head.next.val:
            if head.next.next == None:
                return None
            elif head.val == head.next.next.val:
                return Solution.deleteDuplicates(self, head.next)
            else:
                return Solution.deleteDuplicates(self, head.next.next)
        else:
            return ListNode(head.val, Solution.deleteDuplicates(self, head.next))