# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, head):
        arr = []
        while head != None:
            arr.append(head.val)
            head = head.next
        arr = arr[(len(arr) // 2):]
        arr = arr[::-1]
        ans = None
        while arr != []:
            ans = ListNode(arr[0], ans)
            arr.pop(0)
        return ans