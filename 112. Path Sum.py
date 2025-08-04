# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if root == None:
            return False
        else:
            l = []
            def summer(sum, root):
                if root.left == None and root.right == None:
                    l.append(sum + root.val)
                elif root.left == None:
                    summer(sum + root.val, root.right)
                elif root.right == None:
                    summer(sum + root.val, root.left)
                else:
                    summer(sum + root.val, root.right)
                    summer(sum + root.val, root.left)
            summer(0, root)
            return targetSum in l