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
            nxt_lst = []
            ind = 0
            while ind < len(lst):
                cur = lst[ind]
                if ind != len(lst) - 1:
                    cur.next = lst[ind + 1]
                if cur.left and cur.right:
                    nxt_lst.extend([cur.left, cur.right])
                elif cur.right != None:
                    nxt_lst.append(cur.right)
                elif cur.left != None:
                    nxt_lst.append(cur.left)
                ind += 1
            if nxt_lst != []:
                nextify(nxt_lst)
        if root == None:
            return root
        else:
            nextify([root])
            return root 