# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random
class Solution(object):

    def __init__(self, head):
        copy = head
        ct = 0
        while copy != None:
            ct += 1
            copy = copy.next
        self.length = ct
        self.list = head
        

    def getRandom(self):
        copy = self.list
        r = random.randint(1, self.length)
        while r > 1:
            copy = copy.next
            r -= 1
        return copy.val



# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()