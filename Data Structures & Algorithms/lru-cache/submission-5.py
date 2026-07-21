class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.smth ={}
        self.left = Node(0,0)   # LRU
        self.right = Node(0,0)  # MRU

        self.left.next = self.right
        self.right.prev = self.left

    def movetoend(self,node):
        prev = self.right.prev
        prev.next = node
        node.prev=prev
        node.next=self.right
        self.right.prev = node

    def deleteifmore(self,node ):
        prev = node.prev
        nxt=node.next
        prev.next=nxt
        nxt.prev=prev

        
        

    def get(self, key: int) -> int:

        if key not in self.smth:
            return -1
        node = self.smth[key]
        self.deleteifmore(node)
        self.movetoend(node)

        return node.val
        

    def put(self, key: int, value: int) -> None:

        if key in self.smth:
            node = self.smth[key]
            self.deleteifmore(node)
        self.smth[key]= Node(key,value)
        self.movetoend(self.smth[key])
        
        if len(self.smth) > self.capacity:
            lru = self.left.next
            self.deleteifmore(lru)
            del self.smth[lru.key]

        
