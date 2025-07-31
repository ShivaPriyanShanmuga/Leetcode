# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        result = []

        def helper(node):
            if node:
                helper(node.left)           # Visit left subtree
                result.append(node.val)   # Visit root
                helper(node.right)          # Visit right subtree

        helper(root)
        return result