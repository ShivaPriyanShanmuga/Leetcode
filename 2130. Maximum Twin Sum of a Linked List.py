# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def pairSum(self, head):
        l = []
        rev = None
        cpy = head
        leng = 0
        while cpy:
            rev = ListNode(cpy.val, rev)
            cpy = cpy.next
            leng += 1
        while leng // 2:
            l.append(head.val + rev.val)
            head = head.next
            rev = rev.next
            leng -= 1
        return max(l)
        