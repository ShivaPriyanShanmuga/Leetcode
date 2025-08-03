# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def sortList(self, head):
        l = []
        sorted = None
        while head != None:
            l.append(head.val)
            head = head.next
        l.sort(reverse=True)
        for i in l:
            sorted = ListNode(i, sorted)
        return sorted