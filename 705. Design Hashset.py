class MyHashSet(object):

    def __init__(self):
        self.map = {}

    def add(self, key):
        self.map[key] = ''
        

    def remove(self, key):
        if key in self.map:
            self.map.pop(key)
        

    def contains(self, key):
        return key in self.map
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)