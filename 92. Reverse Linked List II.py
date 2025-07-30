# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def reverseBetween(self, head, left, right):
        a = []
        while head:
            a.append(head.val)
            head = head.next
        rev = a[left - 1:right]
        rev = rev[::-1]
        a[left - 1:right] = rev
        ans = None
        a = a[::-1]
        for i in a:
            ans = ListNode(i, ans)
        return ans
