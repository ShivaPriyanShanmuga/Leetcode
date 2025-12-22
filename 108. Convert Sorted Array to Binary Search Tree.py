# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        def recur(arr):
            if arr == []:
                return None
            elif len(arr) == 1:
                return TreeNode(arr[0], None, None)
            else:
                mid = len(arr) // 2
                return TreeNode(arr[mid], recur(arr[:mid]), recur(arr[mid+1:]))
        return recur(nums)
