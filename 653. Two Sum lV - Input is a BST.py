# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        l = []
        def recurse(root):
            if root == None:
                pass
            else:
                recurse(root.left)
                l.append(root.val)
                recurse(root.right)
        recurse(root)
        for i in range(len(l)):
            for j in range(i + 1, len(l)):
                if l[i] + l[j] == k:
                    return True
                else:
                    pass
        return False
        