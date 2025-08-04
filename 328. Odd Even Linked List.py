# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        if head == None:
            return head
        else:
            length = 0
            copy = head
            even_list = None
            odd_list = None
            l = [None, None]
            while copy:
                copy = copy.next
                length += 1
            if length % 2 == 0:
                while length != 0:
                    if odd_list == None:
                        nxt = head.next
                        head.next = None
                        odd_list = head
                        head = nxt.next
                        nxt.next = None
                        even_list = nxt
                        length -= 2
                        l[0] = odd_list
                        l[1] = even_list
                    else:
                        nxt = head.next
                        head.next = None
                        odd_list.next = head
                        head = nxt.next
                        nxt.next = None
                        even_list.next = nxt
                        length -= 2
                        odd_list = odd_list.next
                        even_list = even_list.next
                odd_list.next = l[1]
                return l[0]
            else:
                if length == 1:
                    return head
                while length != 1:
                    if odd_list == None:
                        nxt = head.next
                        head.next = None
                        odd_list = head
                        head = nxt.next
                        nxt.next = None
                        even_list = nxt
                        length -= 2
                        l[0] = odd_list
                        l[1] = even_list
                    else:
                        nxt = head.next
                        head.next = None
                        odd_list.next = head
                        head = nxt.next
                        nxt.next = None
                        even_list.next = nxt
                        length -= 2
                        odd_list = odd_list.next
                        even_list = even_list.next
                head.next = l[1]
                odd_list.next = head
                return l[0]