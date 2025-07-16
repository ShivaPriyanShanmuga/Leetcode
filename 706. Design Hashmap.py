class MyHashMap(object):

    def __init__(self):
        self.map = {}

    def put(self, key, value):
        self.map[key] = value
        

    def get(self, key):
        if key in self.map:
            return self.map[key]
        else:
            return -1
        

    def remove(self, key):
        if key in self.map:
            self.map.pop(key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)