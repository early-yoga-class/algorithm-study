# 큐 연산(popleft)는 O(1)이라 해도 내부적으로는 연속 메모리 아닌 경우 비용이 큼

# 한 번의 연산 = 한 원소 이동 → 두 큐를 한 덩어리로 붙여서 투 포인터처럼 인덱스를 옮기면서 비교
# 큐를 이어붙여서 순환 구조를 만들고 투 포인터로 슬라이딩 윈도우처럼 탐색하면 deque 연산 없이도 동작할 수 있음
# 최악 시간복잡도 O(2N) 이하로 제한됨

def solution(queue1, queue2):
    total = sum(queue1) + sum(queue2)
    
    if total % 2 != 0:
        return -1

    target = total // 2
    q = queue1 + queue2
    n = len(queue1)

    left = 0
    right = n
    curr = sum(queue1)
    count = 0

    while left < len(q) and right < len(q):
        if curr == target:
            return count
        elif curr < target:
            curr += q[right]
            right += 1
        else:
            curr -= q[left]
            left += 1
        count += 1

    return -1