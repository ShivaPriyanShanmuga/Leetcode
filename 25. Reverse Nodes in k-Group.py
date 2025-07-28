# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        a = []
        ans = []
        fin = []
        while head:
            a.append(head.val)
            head = head.next
        ct = 0
        nxt = k
        while ct < len(a):
            ans.append(a[ct:nxt])
            ct += k
            nxt += k
        for i in ans:
            if len(i) != k:
                fin.extend(i)
            else:
                fin.extend(i[::-1])
        res = None
        print(fin)
        fin = fin[::-1]
        for i in fin:
            res = ListNode(i, res)
        return res
