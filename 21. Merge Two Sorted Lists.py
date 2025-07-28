# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        elif list1.val >= list2.val:
            return ListNode(list2.val, Solution.mergeTwoLists(self, list1, list2.next))
        else:
            return ListNode(list1.val, Solution.mergeTwoLists(self, list1.next, list2))
