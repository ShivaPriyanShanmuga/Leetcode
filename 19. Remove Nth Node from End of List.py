# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        arr = []
        new = None
        while head != None:
            arr.append(head.val)
            head = head.next
        arr = arr[::-1]
        arr.pop(n - 1)
        for i in arr:
            new = ListNode(i, new)
        return new