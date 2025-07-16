# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        stack = []
        original = head
        while head:
            nxt = head.next
            head.next = None
            stack.append(head)
            head = nxt
        fin = []
        if len(stack) % 2 == 0:
            for i in range(len(stack)//2):
                fin.append(stack[i])
                fin.append(stack[-i - 1])
        else:
            for i in range((len(stack) - 1)//2):
                fin.append(stack[i])
                fin.append(stack[-i - 1])
            fin.append(stack[(len(stack) - 1)//2])
        head = fin[0]
        copy = head
        for i in range(1, len(fin)):
            copy.next = fin[i]
            copy = copy.next