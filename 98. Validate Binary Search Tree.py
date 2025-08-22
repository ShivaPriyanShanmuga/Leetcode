# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isValidBST(self, root):
        l = []
        def inorder(root):
            if root == None:
                pass
            else:
                inorder(root.left)
                l.append(root.val)
                inorder(root.right)
        inorder(root)
        for i in range(len(l)):
            if i != len(l) - 1:
                if l[i] < l[i + 1]:
                    pass
                else:
                    return False
        return True