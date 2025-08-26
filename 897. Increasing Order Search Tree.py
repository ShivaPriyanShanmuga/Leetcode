# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def increasingBST(self, root):
        l = []
        def recurse(root):
            if root == None:
                pass
            else:
                recurse(root.right)
                l.append(root.val)
                recurse(root.left)
        recurse(root)
        def recursive():
            if l:
                return TreeNode(l.pop(), None, recursive())
            else:
                None
        return recursive()

