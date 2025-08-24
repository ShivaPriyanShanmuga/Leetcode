"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        def length(root, sum):
            if root == None:
                return 0
            elif root.children:
                l = []
                for i in root.children:
                    l.append(length(i, sum + 1))
                return max(l)
            else:
                return 1 + sum
        return length(root, 0)