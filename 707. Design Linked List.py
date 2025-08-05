class MyLinkedList(object):

    def __init__(self):
        self.list = []
        self.length = 0

    def get(self, index):
        if index <= self.length - 1:
            return self.list[index]
        else:
            return -1

    def addAtHead(self, val):
        self.length += 1
        self.list = [val] + self.list

    def addAtTail(self, val):
        self.length += 1
        self.list.append(val)
        

    def addAtIndex(self, index, val):
        if index <= self.length:
            self.list.insert(index, val)
            self.length += 1

    def deleteAtIndex(self, index):
        if index < self.length:
            self.list.pop(index)
            self.length -= 1

'''
Alternate Solution below
'''

# class MyLinkedList(object):
#     def __init__(self):
#         self.list = ()
#         self.length = 0

#     def get(self, index):
#         if index > self.length - 1:
#             return -1
#         else:
#             cpy = self.list
#             while index > 0:
#                 cpy = cpy[1]
#                 index -= 1
#             return cpy[0] 

#     def addAtHead(self, val):
#         self.length += 1
#         self.list = (val, self.list)

#     def addAtTail(self, val):
#         if self.list == ():
#             self.list = (val, ())
#             self.length += 1
#         else:
#             self.length -= 1
#             initial = self.list[0]
#             self.list = self.list[1]
#             MyLinkedList.addAtTail(self, val)
#             self.list = (initial, self.list)
#             self.length += 1

#     def addAtIndex(self, index, val):
#         if index <= self.length:
#             if index == 0:
#                 self.length += 1
#                 self.list = (val, self.list)
#             else:
#                 self.length -= 1
#                 initial = self.list[0]
#                 self.list = self.list[1]
#                 MyLinkedList.addAtIndex(self, index - 1, val)
#                 self.list = (initial, self.list)
#                 self.length += 1

#     def deleteAtIndex(self, index):
#         if index <= self.length - 1:
#             if index == 0:
#                 self.length -= 1
#                 self.list = self.list[1]
#             else:
#                 self.length -= 1
#                 initial = self.list[0]
#                 self.list = self.list[1]
#                 MyLinkedList.deleteAtIndex(self, index - 1)
#                 self.list = (initial, self.list)
#                 self.length += 1
        


# # Your MyLinkedList object will be instantiated and called as such:
# # obj = MyLinkedList()
# # param_1 = obj.get(index)
# # obj.addAtHead(val)
# # obj.addAtTail(val)
# # obj.addAtIndex(index,val)
# # obj.deleteAtIndex(index)