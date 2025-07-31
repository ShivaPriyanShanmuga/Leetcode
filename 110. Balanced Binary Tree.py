# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def isBalanced(self, root):
        if root == None:
            return True
        elif abs(Solution.height(self, root.left) - Solution.height(self, root.right)) <= 1:
            return Solution.isBalanced(self, root.left) and Solution.isBalanced(self, root.right)
        else:
            return False
    def height(self, root):
        if root == None:
            return 0
        else:
            return 1 + max(Solution.height(self, root.left), Solution.height(self, root.right))