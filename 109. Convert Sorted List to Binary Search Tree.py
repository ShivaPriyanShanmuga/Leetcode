# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedListToBST(self, head):
        l = []
        while head:
            l.append(head.val)
            head = head.next
        def make_tree(lst):
            if lst == []:
                return None
            else:
                mid = len(lst) // 2
                left_part = lst[:mid]
                right_part = lst[mid + 1:]
                return TreeNode(lst[mid], make_tree(left_part), make_tree(right_part))
        return make_tree(l)