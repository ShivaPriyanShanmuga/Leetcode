# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        ptr = head
        cpy = head
        n = 0
        while cpy != None:
            n += 1
            cpy = cpy.next
        index = n // 2
        prev = None
        while index > 0:
            index -= 1
            if prev == None:
                nxt = head.next
                head.next = None
                prev = head
                head = nxt
            else:
                nxt = head.next
                head.next = None
                prev.next = head
                prev = prev.next
                head = nxt
        if prev != None:
            prev.next = head.next
        else:
            return None
        return ptr