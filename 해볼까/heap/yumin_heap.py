class MinHeap():
    def __init__(self):
        # heap이라는 변수가 있음
        self.heap = []

    def push(self,value):
        # 리스트 끝자락에 append
        self.heap.append(value)
        self._sift_up(len(self.heap)-1)

    def pop(self):
        if not self.heap:
            raise IndexError("pop from empty heap")
        # pop 시키려면 끝으로 가야됨. 제일 큰 값과 바꾼다.
        self._swap(0,len(self.heap)-1)
        # 제일 큰 값 -> 작은 값 pop 한다.
        min_value = self.heap.pop() 
        # 루트에서 내려오면서 자리 찾아감
        self._sift_down(0)
        return min_value
    
    def peek(self):
        if not self.heap:
            raise IndexError("peek from empty heap")
        return self.heap[0]

    def _sift_up(self,idx):
        # 현재 새로 들어온 값의 idx를 받아온다.
        parent = (idx -1)//2
        # 부모 인덱스를 구한다! 부모모다 작으면 부모랑 자리 교체 후, 올라감.
        if idx > 0 and self.heap[idx] < self.heap[parent]:
            self._swap(idx,parent)
            # 부모 자리바꿨으니깐 또 체크함.
            self._sift_up(parent)

    def _sift_down(self,idx):
        left = 2*idx + 1
        right = 2*idx + 2
        smallest =idx
        
        # 자식보다 크면 내려간다.
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        # 이동했으면? 바꿔주고 또 내려간다. 체크!
        if smallest != idx:
            self._swap(self,idx,smallest)
            self._sift_down(self,smallest)
    
    def _swap(self, i, j):
        # 인덱스로 위치 바꾸기
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __len__(self):
        return len(self.heap)
    
    def __str__(self):
        return str(self.heap)