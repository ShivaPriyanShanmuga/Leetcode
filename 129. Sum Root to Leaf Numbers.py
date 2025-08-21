# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sumNumbers(self, root):
        l = []
        def recursive(root, num):
            if root == None:
                pass
            elif root.left == None and root.right == None:
                l.append(int(num + str(root.val)))
            else:
                num += str(root.val)
                recursive(root.left, num[:])
                recursive(root.right, num)
        recursive(root, '')
        return sum(l)
        