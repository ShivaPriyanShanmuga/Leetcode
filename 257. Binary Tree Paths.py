# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        l = []
        def recurse(root, lst):
            if root == None:
                pass
            elif root.left == None and root.right == None:
                lst.append(str(root.val))
                l.append(lst)
            else:
                lst.append(str(root.val))
                recurse(root.left, lst[:])
                recurse(root.right, lst[:])
        recurse(root, [])
        for i in range(len(l)):
            l[i] = "->".join(l[i])
        return l