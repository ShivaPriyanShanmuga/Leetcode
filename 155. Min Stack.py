class MinStack(object):

    def __init__(self):
        self.stack = []
        self.hashmap = {}
    def push(self, val):
        self.stack.append(val)
        if val in self.hashmap:
            self.hashmap[val] += 1
        else:
            self.hashmap[val] = 1

    def pop(self):
        elem = self.stack.pop()
        self.hashmap[elem] -= 1
        if self.hashmap[elem] == 0:
            self.hashmap.pop(elem)
        
    def top(self):
        return self.stack[-1]
        
    def getMin(self):
        return min(self.hashmap)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()