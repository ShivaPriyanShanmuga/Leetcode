# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSymmetric(self, root):
        def compare(rootl, rootr):
            if rootl == None and rootr == None:
                return True
            elif rootl == None or rootr == None:
                return False
            elif rootl.val == rootr.val:
                return compare(rootl.left, rootr.right) and compare(rootl.right, rootr.left)
            else:
                return False
        return compare(root.left, root.right)