# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        l = []
        def recurse(lst):
            new_l = []
            val_l = []
            for i in lst:
                if i.left == None and i.right == None:
                    pass
                elif i.left == None:
                    new_l.append(i.right)
                elif i.right == None:
                    new_l.append(i.left)
                else:
                    new_l.extend([i.left, i.right])
                val_l.append(i.val)
            l.append(val_l)
            if new_l:
                recurse(new_l)
        if root:
            recurse([root])
        return l[::-1]
        