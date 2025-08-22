# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def levelOrder(self, root):
        l = []
        def traverse(lst):
            new_l = []
            val_lst = []
            for i in lst:
                if i.left == None and i.right == None:
                    pass
                elif i.left == None:
                    new_l.append(i.right)
                elif i.right == None:
                    new_l.append(i.left)
                else:
                    new_l.extend([i.left, i.right])
                val_lst.append(i.val)
            l.append(val_lst)
            if new_l == []:
                pass
            else:
                traverse(new_l)
        if root == None:
            return l
        else:
            traverse([root])
        return l