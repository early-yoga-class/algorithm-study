class DoubleLinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.beforeNode = None
            self.nextNode = None

    def __init__(self):
        self.tail = None
        self.head = None
        self.size =0

    def __len__(self):
        return self.size

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.nextNode

    @classmethod
    def Deque(cls, numbers):
        obj = cls()
        prev = None
        for i, num in enumerate(numbers):
            node = obj.Node(num)
            if i == 0:
                obj.head = node
            else:
                node.beforeNode = prev
                prev.nextNode = node
            prev = node
        obj.tail = prev
        obj.size = len(numbers)
        return obj


    def append(self, node):
        if type(node) is not self.Node:
            node = self.Node(node)

        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.nextNode = node
            node.beforeNode = self.tail
            self.tail = node
        self.size+=1

    def appendLeft(self, node):
        if type(node) is not self.Node:
            node = self.Node(node)

        if self.head is None:
            self.head = self.tail = node
        else:
            self.head.beforeNode = node
            node.nextNode = self.head
            self.head = node

        self.size+=1

    def popRight(self):
        if self.size == 0:
            raise IndexError("리스트가 비어있습니다.")
        result = self.tail
        self.tail.beforeNode.nextNode = None
        self.tail = self.tail.beforeNode
        self.size-=1
        return result.value

    def pop(self):
        if self.size == 0:
            raise IndexError("리스트가 비어있습니다.")
        result = self.head
        self.head.nextNode.beforeNode= None
        self.head = self.head.nextNode
        self.size-=1
        return result.value

    def insert(self, idx, value):
        if idx<0 or idx>self.size:
            raise IndexError("인덱스 오류")

        if idx == 0:
            self.appendLeft(value)
        elif idx == self.size:
            self.append(value)
        else:
            node = self.Node(value)
            current = self.head
            for _ in range(idx):
                current = current.nextNode
            prev, prev.nextNode  = current.beforeNode, node
            node.beforeNode, node.nextNode = prev, current
            current.beforeNode = node
            self.size += 1

    def remove(self, value):
        current = self.head
        for i in range(self.size):
            if current.value == value:
                current.beforeNode.nextNode = current.nextNode
                current.nextNode.beforeNode = current.beforeNode
                self.size -=1
                return current.value
            else:
                current = current.nextNode
        raise ValueError(f"{value}를 찾지 못했습니다.")

    def removeByIndex(self, idx):
        if idx< 0 or idx>self.size:
            raise IndexError("인덱스가 잘못되었습니다.")
        current = self.head
        for i in range(idx):
            if i == idx-1:
                current.beforeNode.nextNode = current.nextNode
                current.nextNode.beforeNode = current.beforeNode
                self.size-=1
                return current.value
            else:
                current = current.nextNode