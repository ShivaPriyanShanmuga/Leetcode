# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        l1 = []
        l2 = []
        def recurse(root, l):
            if root == None:
                pass
            elif root.left == None and root.right == None:
                l.append(root.val)
            else:
                recurse(root.left, l)
                recurse(root.right, l)
        recurse(root1, l1)
        recurse(root2, l2)
        return l1 == l2