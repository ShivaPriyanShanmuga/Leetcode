# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def modifiedList(self, nums, head):
        hashmap = {}
        for i in nums:
            hashmap[i] = ''
        l = []
        while head:
            if head.val in hashmap:
                head = head.next
            else:
                nxt = head.next
                head.next = None
                l.append(head)
                head = nxt
        res = None
        while l:
            popped = l.pop()
            popped.next = res
            res = popped
        return res
        