class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insert(self,node):
        next_node = self.head.next

        node.prev = self.head
        node.next = next_node

        next_node.prev = node
        self.head.next = node
    
    def get(self, key):
        if not key in self.cache:
            return -1

        node = self.cache[key]

        self.remove(node)

        self.insert(node)
        
        return node.value
    
    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
        
        new_node = Node(key, value)
        
        self.insert(new_node)

        self.cache[key] = new_node
        
        if len(self.cache) > self.capacity:
            lru_node = self.tail.prev

            self.remove(lru_node)

            del self.cache[lru_node.key]

cache = LRUCache(2)

cache.put(1, "A")

cache.put(2, "B")

a = cache.get(1)

print(a)

cache.put(3, "C")

b = cache.get(2)

print(b)
