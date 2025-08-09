# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def invertTree(self, root):
        if root == None:
            return None
        elif root.left == None and root.right == None:
            return TreeNode(root.val)
        else:
            return TreeNode(root.val, Solution.invertTree(self, root.right), Solution.invertTree(self, root.left))