# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        def recurse(root, cloned):
            if root == None:
                pass
            elif root == target:
                return cloned
            else:
                val1 = recurse(root.left, cloned.left)
                val2 = recurse(root.right, cloned.right)
                if val1:
                    return val1
                else:
                    return val2
        return recurse(original, cloned)
        