"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        l = []
        def appender(head):
            while head:
                nxt = head.next
                head.next = None
                head.prev = None
                if head.child:
                    child = head.child
                    head.child = None
                    l.append(head)
                    appender(child)
                    head = nxt
                else:
                    l.append(head)
                    head = nxt
        appender(head)
        res = None
        while l:
            popped = l.pop()
            popped.next = res
            if res:
                res.prev = popped
            res = popped
        return res