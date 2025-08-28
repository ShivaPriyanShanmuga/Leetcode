# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        def traverse(lst):
            new_l = []
            val_l = []
            for i in lst:
                if i.left == None and i.right == None:
                    val_l.append(i.val)
                elif i.left == None:
                    new_l.append(i.right)
                    val_l.append(i.val)
                elif i.right == None:
                    new_l.append(i.left)
                    val_l.append(i.val)
                else:
                    new_l.extend([i.left, i.right])
                    val_l.append(i.val)
            if new_l:
                return traverse(new_l)
            else:
                return val_l[0]
        
        return traverse([root])