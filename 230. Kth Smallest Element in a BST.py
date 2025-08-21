# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        l = []
        def accessor(root):
            if root == None:
                pass
            else:
                accessor(root.left)
                l.append(root.val)
                accessor(root.right)
        accessor(root)
        return l[k - 1]
        