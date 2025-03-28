class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, value):
        new = Node(value)
        if self.is_empty():
            self.head = new
            self.tail = new
        else :
            self.tail.next = new
            new.prev = self.tail
            self.tail = new
        self.size += 1
        
    def appendleft(self, value):
        new = Node(value)
        if self.is_empty():
            self.head = new
            self.tail = new
        else :
            self.head.prev = new
            new.next = self.head
            self.head = new
        self.size += 1

    def pop(self):
        if self.is_empty():
            return -1
        give = self.tail.value
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
        return give
    
    def popleft(self):
        if self.is_empty():
            return -1
        give = self.head.value
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -=1
        return give

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

dq = Deque()
dq.append(1)
dq.append(2)
dq.appendleft(0)
print(dq.popleft())  # 0
print(dq.pop())      # 2
print(dq.pop())      # 1
print(dq.pop())      # -1
print(len(dq))       # 0
