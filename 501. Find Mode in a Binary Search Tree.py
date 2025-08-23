# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        l = []
        def recurse(root):
            if root == None:
                pass
            else:
                recurse(root.left)
                recurse(root.right)
                l.append(root.val)
        recurse(root)
        hashmap = {}
        for i in l:
            if l.count(i) in hashmap and i not in hashmap[l.count(i)]:
                hashmap[l.count(i)].append(i)
            elif l.count(i) not in hashmap:
                hashmap[l.count(i)] = [i]
        return hashmap[max(hashmap)]