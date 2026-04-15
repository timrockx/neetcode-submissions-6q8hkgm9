class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):

        self.capacity = capacity
        self.cache = {}
        
        self.start = Node(0, 0)
        self.end = Node(0, 0)
        self.start.next = self.end
        self.end.prev = self.start

    def get(self, key: int) -> int:

        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
    
    def insert(self, node):
        prev, next = self.end.prev, self.end
        prev.next = node
        node.prev = prev
        node.next = next
        next.prev = node

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.remove(self.cache[key])

        new_node = Node(key, value)
        self.cache[key] = new_node
        self.insert(new_node)

        if len(self.cache) > self.capacity:
            lru = self.start.next
            self.remove(lru)
            del self.cache[lru.key]
        
