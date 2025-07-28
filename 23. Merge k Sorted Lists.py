# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        a = []
        for i in lists:
            while i != None:
                a.append(i.val)
                i = i.next
        a.sort(reverse=True)
        ans = None
        for i in a:
            ans = ListNode(i, ans)
        return ans
        
        