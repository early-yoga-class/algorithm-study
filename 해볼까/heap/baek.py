
class MinHeap:
    def __init__(self): 
        self.heap = []

    def __str__(self):
        return str(self.heap)

    def push(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap)-1)
    
    def pop(self):
        if self.is_empty():
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root_val
    
    def is_empty(self):
        return len(self.heap) == 0
        
    def peek(self):
        if self.is_empty():
            return None
        return self.heap[0]
    
    def size(self):
        return len(self.heap)
        
        
    def _heapify_up(self, idx):
        parent = (idx-1) // 2
        if idx > 0 and self.heap[idx] < self.heap[parent]:
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            self._heapify_up(parent)
    
    def _heapify_down(self, idx):
        left = idx*2 + 1
        right = idx*2 + 2
        smallest = idx
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != idx:
            self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
            self._heapify_down(smallest)            
    
    @classmethod
    def heapify(cls, arr):
        instance = cls()
        instance.heap = arr[:]
        for i in range(len(instance.heap) // 2 - 1, -1, -1):
            instance._heapify_down(i)
        return instance    

A = MinHeap.heapify([1, 5, 6, 3, 10])
print(A)

A.pop()
print(A)

A.push(4)
print(A)