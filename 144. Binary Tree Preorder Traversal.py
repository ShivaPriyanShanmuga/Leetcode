# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        l = []
        def recurse(root):
            if root == None:
                pass
            else:
                l.append(root.val)
                recurse(root.left)
                recurse(root.right)
        recurse(root)
        return l
        