class MinHeap:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)
        self.bubbleUp()

    def pop(self):
        if self.size() == 0:
            return None
        minvalue = self.items[0]
        self.items[0] = self.items[-1]
        self.items.pop()
        self.bubbleDown()
        return minvalue

    def peek(self):
        return self.items[0] if self.items else None

    def bubbleUp(self):
        idx = self.size() - 1
        while idx > 0:
            parent_idx = (idx - 1) // 2
            if self.items[parent_idx] <= self.items[idx]: break
            self.items[idx], self.items[parent_idx] = self.items[parent_idx], self.items[idx]
            idx = parent_idx

    def bubbleDown(self, idx=0):
        size = self.size()
        while idx * 2 + 1 < size:
            left_child = idx * 2 + 1
            right_child = idx * 2 + 2
            smaller_child = right_child if (right_child < size and
                                            self.items[right_child] < self.items[left_child]) else left_child

            if self.items[idx] <= self.items[smaller_child]: break

            self.items[idx], self.items[smaller_child] = self.items[smaller_child], self.items[idx]
            idx = smaller_child

    def __str__(self):
        return " ".join(str(data) for data in self.items)

    @classmethod
    def heapify(cls, array):
        heap = cls()
        heap.items = array[:]
        for idx in range(len(array) // 2 - 1, -1, -1):
            heap.bubbleDown(idx)
        return heap


mh = MinHeap()

mh.push(13)
mh.push(19)
mh.push(3)
mh.push(2)
print(mh.peek())
print(mh.size())
print(str(mh))

print(MinHeap.heapify([200, 19, 23, 43, 24]))

