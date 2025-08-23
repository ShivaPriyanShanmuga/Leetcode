# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        sum = [0]
        def recurse(root, string):
            if root == None:
                pass
            elif root.left == None and root.right == None:
                sum[0] += int(string + str(root.val), 2)
            else:
                string += str(root.val)
                recurse(root.left, string)
                recurse(root.right, string)
        recurse(root, '0b')
        return sum[0]
        