class DoublyLinkedList:
    class Node:
        def __init__(self, data):
            self.prev = None
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        """오른쪽 끝에 데이터를 추가합니다"""
        new_node = self.Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def appendleft(self, data):
        """왼쪽 끝에 데이터를 추가합니다"""
        new_node = self.Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def pop(self):
        """오른쪽 끝 데이터를 삭제하여 반환합니다"""
        if self.head is None:
            raise IndexError("삭제할 데이터가 존재하지 않습니다")

        delete_node = self.tail

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
        return delete_node.data

    def popleft(self):
        """왼쪽 끝 데이터를 삭제하여 반환합니다"""
        if self.head is None:
            raise IndexError("삭제할 데이터가 존재하지 않습니다")

        delete_node = self.head

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
        return delete_node.data

    def peek(self):
        """가장 오른쪽 데이터 값을 조회합니다"""
        if self.head is None:
            raise IndexError("데이터가 존재하지 않습니다")
        return self.tail.data

    def peekleft(self):
        """가장 왼쪽 데이터 값을 조회합니다"""
        if self.head is None:
            raise IndexError("데이터가 존재하지 않습니다")
        return self.head.data

    def is_empty(self):
        """큐가 비어있는지 확인합니다"""
        return self.size == 0

    def __len__(self):
        return self.size

    def clear(self):
        """연결된 모든 노드들을 삭제합니다"""
        self.head = None
        self.tail = None
        self.size = 0

    def __iter__(self):
        """정방향 순회 이터레이터"""
        return DoublyLinkedListIterator(self.head)

    def __reversed__(self):
        """역방향 순회 이터레이터"""
        return DoublyLinkedListIterator(self.tail, False)

    def __str__(self):
        """
        연결 리스트 전체 데이터를 문자열로 반환
        __iter__()로 순회하면서 각 데이터를 문자열로 변환,
        ' <-> ' 구분자로 연결

        참고 : 직접 순회 방식 예시
        ----------------------
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return " <-> ".join(result)
        """
        return " <-> ".join(str(data) for data in self)


class DoublyLinkedListIterator:
    """이중 연결 리스트 순회를 위한 이터레이터 클래스"""
    def __init__(self, head, forward=True):
        self.current = head
        self.forward = forward

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration

        data = self.current.data
        self.current = self.current.next if self.forward else self.current.prev
        return data