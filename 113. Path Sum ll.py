# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        l = []
        def recursor(root, sum, targetSum, lst):
            if root == None:
                pass
            elif root.left == None and root.right == None:
                if sum + root.val == targetSum:
                    lst.append(root.val)
                    l.append(lst)
            else:
                lst.append(root.val)
                sum += root.val
                recursor(root.left, sum, targetSum, lst[:])
                recursor(root.right, sum, targetSum, lst)
        recursor(root, 0, targetSum, [])
        return l