# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        l = []
        def gcd(greater, lesser):
            if greater % lesser == 0:
                l.append(lesser)
            else:
                gcd(lesser, greater % lesser)
        tmp = head
        while tmp.next:
            gcd(max(tmp.val, tmp.next.val), min(tmp.val, tmp.next.val))
            tmp = tmp.next
        tmp1 = head
        ind = 0
        while ind < len(l):
            nxt = tmp1.next
            tmp1.next = ListNode(l[ind], nxt)
            tmp1 = nxt
            ind += 1
        return head