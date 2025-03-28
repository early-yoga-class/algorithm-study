# 노드 = 데이터 + 포인터 정보
class Node:
    def __init__(self,data):
        # 아직은 전후 포인터가 비어있다.
        self.data = data
        self.prev = None
        self.next = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self,value):
        # 일단은 노드 인스턴스 부터 만든다. (리스트는 별개)
        new_node = Node(value)
        # 현재 리스트에서 꼬리가 없으면 = lst 비어있으면 ?  새로만든다.
        if self.tail is None:
            # 리스트의 head 와 tail을 현재 노드로 지정해준다.
            self.head = self.tail = new_node
        else:
            # 만약 이미 존재한다면? 리스트에서 현재 꼬리의 다음포인터를 new_node로 지정해준다.
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        # 리스트 길이 늘린다.
        self.length += 1
    
    def appendleft(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def pop(self):
        if self.tail is None:
            raise IndexError("pop from empty deque")
        value = self.tail.data
        # 꼬리 이전으로 바꿔준다.
        self.tail = self.tail.prev
        #값이 하나였다면? head 도 None으로 바꿔준다.
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None
        self.length -= 1
        return value

    def popleft(self):
        if self.head is None:
            raise IndexError("pop from empty deque")
        value = self.head.data
        # 머리를 이후로 바꿔준다.
        self.head = self.tail.next
        #값이 하나였다면? head 도 None으로 바꿔준다.
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        self.length -= 1
        return value
    
    def __len__(self):
        return self.length
    
    def is_empty(self):
        return self.length == 0
    
    def __contains(self,target):
        node = self.head
        while node:
            if node.data == target:
                return True
            node = node.next
        return False
    
    # 사람이 알아보기 힘든 문자열로 이루어져 있음. 문자열로 바꿔서 return
    def __str__(self):
        if self.is_empty():
            return "Empty!"
        result = []
        node = self.head
        # 앞머리를 node로 저장
        while node:
            result.append(str(node.data))
            node = node.next
        return " ↔ ".join(result)
