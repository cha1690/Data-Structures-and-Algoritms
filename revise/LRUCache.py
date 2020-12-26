class LinkedList:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity):
        self.store = {}
        self.capacity = capacity
        self.head = LinkedList(-1,-1)
        self.tail = LinkedList(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.store:
            node = self.store[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key, value):
        if key in self.store:
            node = self.store[key]
            self.remove(node)
        else:
            if len(self.store) == self.capacity:
                lru_node=self.head.next
                self.remove(lru_node)
                del(self.store[lru_node.key])
        node=LinkedList(key, value)
        self.store[key]=value
        self.insert(node)


    def insert(self, node):
        pre = self.tail.prev
        pre.next = node
        node.next = self.tail
        self.tail.prev = node
        node.prev = pre

    def remove(self, node):
        pre= self.node.prev
        nxt = self.node.next
        pre.next= nxt
        nxt.prev= pre

