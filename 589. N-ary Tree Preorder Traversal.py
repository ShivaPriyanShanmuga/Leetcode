"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        l = []
        def recurse(root):
            if root == None:
                pass
            elif root.children:
                l.append(root.val)
                for i in root.children:
                    recurse(i)
            else:
                l.append(root.val)
        recurse(root)
        return l
        