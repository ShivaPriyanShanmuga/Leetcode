# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        l = []
        def traverse(lst, swap):
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
            if swap:
                l.append(val_lst[::-1])
            else:
                l.append(val_lst)
            if new_l == []:
                pass
            else:
                traverse(new_l, not(swap))
        if root == None:
            return l
        else:
            traverse([root], False)
        return l