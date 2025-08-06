# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution(object):
    def connect(self, root):
        def nextify(lst):
            first = lst[0]
            ind = 0
            if first.left:
                new_lst = []
                while ind <= len(lst) - 1:
                    if ind != len(lst) - 1:
                        new_lst.extend([lst[ind].left, lst[ind].right])
                        lst[ind].next = lst[ind + 1]
                    else:
                        new_lst.extend([lst[ind].left, lst[ind].right])
                    ind += 1
                nextify(new_lst)
            else:
                while ind <= len(lst) - 1:
                    if ind != len(lst) - 1:
                        lst[ind].next = lst[ind + 1]
                    ind += 1
        if root == None:
            return root
        else:
            nextify([root])
            return root