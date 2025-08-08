# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def doubleIt(self, head):
        if head.val == 0:
            return ListNode(0, None)
        else:
            rev = None
            while head:
                nxt = head.next
                head.next = rev
                rev = head
                head = nxt
            def addone(head):
                if head:
                    summed = head.val + 1
                    if summed == 10:
                        return ListNode(0, addone(head.next))
                    else:
                        return ListNode(summed, head.next)
                else:
                    return ListNode(1, None)
            def recursive(head):
                if head:
                    prod = head.val * 2
                    if prod >= 10:
                        rem = prod % 10
                        return ListNode(rem, addone(recursive(head.next)))
                    else:
                        return ListNode(prod, recursive(head.next))
                else:
                    return None
            rev = recursive(rev)
            final = None
            while rev:
                nxt = rev.next
                rev.next = final
                final = rev
                rev = nxt
            return final