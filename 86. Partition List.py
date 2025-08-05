# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        assembler = None
        ptr_assembler = None
        lesser = None
        ptr_lesser = None
        while head:
            nxt = head.next
            head.next = None
            if head.val >= x:
                if not assembler:
                    assembler = head
                    ptr_assembler = assembler
                else:
                    assembler.next = head
                    assembler = assembler.next
            else:
                if not lesser:
                    lesser = head
                    ptr_lesser = lesser
                else:
                    lesser.next = head
                    lesser = lesser.next
            head = nxt
        if ptr_assembler == None and ptr_lesser == None:
            return None
        elif ptr_lesser == None:
            return ptr_assembler
        else:
            lesser.next = ptr_assembler
            return ptr_lesser