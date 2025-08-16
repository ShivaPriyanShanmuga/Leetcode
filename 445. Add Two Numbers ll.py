# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def rev(self, l):
        res = None
        while l:
            res = ListNode(l.val, res)
            l = l.next
        return res
    def sum(self, l1, l2):
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        elif l1.val + l2.val >= 10:
            return ListNode(l1.val + l2.val - 10, Solution.sum(self, l1.next, Solution.sum(self, l2.next, ListNode(1, None))))
        else:
            return ListNode(l1.val + l2.val, Solution.sum(self, l1.next, l2.next))
    def addTwoNumbers(self, l1, l2):
        l1 = Solution.rev(self, l1)
        l2 = Solution.rev(self, l2)
        return Solution.rev(self, Solution.sum(self, l1, l2))
        