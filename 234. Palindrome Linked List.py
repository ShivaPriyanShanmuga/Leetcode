# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        h = head
        rev = None
        while h != None:
            rev = ListNode(h.val, rev)
            h = h.next
        while rev != None:
            if rev.val == head.val:
                rev = rev.next
                head = head.next
            else:
                return False
        return True