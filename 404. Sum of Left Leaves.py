# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        l = [0]
        def summer(root):
            if root == None:
                pass
            elif root.left:
                if root.left.left == None and root.left.right == None:
                    l[0] += root.left.val
                else:
                    summer(root.left)
                summer(root.right)
            else:
                summer(root.right)
        summer(root)
        return l[0]