"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        l = []
        def recurse(lst):
            new_l = []
            val_l = []
            for i in lst:
                if i.children:
                    new_l.extend(i.children)
                val_l.append(i.val)
            l.append(val_l)
            if new_l:
                recurse(new_l)
        if root:
            recurse([root])
        return l
        