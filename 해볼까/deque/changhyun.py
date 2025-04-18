from deque.changhyun_dll import DoublyLinkedList


class Deque:
    def __init__(self):
        self.dll = DoublyLinkedList()

    def append(self, data):
        self.dll.append(data)

    def appendleft(self, data):
        self.dll.appendleft(data)

    def pop(self):
        return self.dll.pop()

    def popleft(self):
        return self.dll.popleft()

    def peek(self):
        return self.dll.peek()

    def peekleft(self):
        return self.dll.peekleft()

    def is_empty(self):
        return self.dll.is_empty()

    def clear(self):
        return self.dll.clear()

    def __len__(self):
        return len(self.dll)

    def __iter__(self):
        return iter(self.dll)

    def __reversed__(self):
        return reversed(self.dll)

    def __str__(self):
        return str(self.dll)



deque = Deque()

deque.append(13)
deque.appendleft(7)
deque.appendleft(33)
deque.appendleft(4)
deque.appendleft(41)
deque.appendleft(9)
print(deque.pop())
print(str(deque))

for data in reversed(deque):
    print(data, end=' ')
print()

for data in deque:
    print(data, end=' ')
print()

print("Before clear:", deque)
deque.clear()
print("After clear:", deque)