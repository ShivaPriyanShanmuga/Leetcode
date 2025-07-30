# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def len(self, head):
        ct = 0
        while head:
            ct += 1
            head = head.next
        return ct
    def rotateRight(self, head, k):
        if head == None or k == 0 or head.next == None:
            return head
        else:
            k = k % Solution.len(self, head)
            h = head
            while k:
                while head.next.next:
                    head = head.next
                inwrds = head.next.val
                head.next = None
                h = ListNode(inwrds, h)
                head = h
                k -= 1
            return h