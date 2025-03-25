class PriorityQueue:
    class Node:
        def __init__(self, priority, value):
            self.priority = priority
            self.value = value
    def __init__(self):
        self.nodes = []

    def heapify(self):
        n = len(self.nodes)
        for i in range((n - 2) // 2, -1, -1):
            self.bubbleDown(i)

    def push(self, priority, val):
        self.nodes.append(self.Node(priority,val))
        self.bubbleUp(len(self.nodes)-1)

    def pop(self):
        if len(self.nodes) == 0:
            raise IndexError("리스트가 비어있습니다.")
        top = self.nodes[0]
        last = self.nodes.pop()
        self.nodes[0] = last
        self.bubbleDown(0)
        return top

    @classmethod
    def PriorityQueue(cls, numbers):
        obj = cls()
        obj.nodes = [obj.Node(priority, value) for priority, value in numbers]
        obj.heapify()
        return obj

    def bubbleUp(self, idx):
        while idx > 0 and self.nodes[idx].priority > self.nodes[(idx-1)//2].priority:
            self.nodes[idx], self.nodes[(idx-1)//2] = self.nodes[(idx-1)//2], self.nodes[idx]
            idx = (idx-1) // 2

    def bubbleDown(self, idx):
        lastIdx = len(self.nodes)-1
        while True:
            left = idx * 2 + 1
            right = idx * 2 + 2
            largest = idx
            if left <= lastIdx and self.nodes[left].priority > self.nodes[largest].priority:
                largest = left
            if right <= lastIdx and self.nodes[right].priority > self.nodes[largest].priority:
                largest = right

            if largest == idx:
                break
            self.nodes[largest], self.nodes[idx] = self.nodes[idx], self.nodes[largest]
            idx = largest
