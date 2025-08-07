# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNodes(self, head):
        rev = None
        while head:
            nxt = head.next
            head.next = rev
            rev = head
            head = nxt
        node_lst = []
        max_elem = 0
        while rev:
            if max_elem > rev.val:
                rev = rev.next
            else:
                max_elem = rev.val
                nxt = rev.next
                rev.next = None
                node_lst.append(rev)
                rev = nxt
        final = None
        node_lst = node_lst[::-1]
        while node_lst:
            popped = node_lst.pop()
            popped.next = final
            final = popped
        return final