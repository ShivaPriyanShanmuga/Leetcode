# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def minDepth(self, root):
        if root == None:
            return 0
        elif root.left == None:
            return 1 + Solution.minDepth(self, root.right)
        elif root.right == None:
            return 1 + Solution.minDepth(self, root.left)
        else:
            return 1 + min(Solution.minDepth(self, root.left), Solution.minDepth(self, root.right))
        