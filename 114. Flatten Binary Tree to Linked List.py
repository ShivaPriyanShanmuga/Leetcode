# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def flatten(self, root):
        l = []
        def bt_to_list(root):
            if root != None:
                lft = root.left
                rgt = root.right
                root.left = None
                root.right = None
                l.append(root)
                bt_to_list(lft)
                bt_to_list(rgt)
        bt_to_list(root)
        def treeify(lst):
            if lst == []:
                return None
            else:
                first = lst.pop()
                first.right = treeify(lst)
                return first
        return treeify(l[::-1])