from collections import deque
def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    answer = -2
    # 1. 각 큐의 합을 구합니다
    total = sum(q1) + sum(q2)
    # 2-0. 홀수일때는?
    if total % 2 != 0:
        return -1
    firstSum = sum(q1)
    secondSum = sum(q2)
    cnt = 0
    while firstSum != secondSum:
        # 만약 둘중 한 큐에 원소가 모두 사라졌다면 break
        if firstSum == 0 or secondSum == 0: return -1
        if cnt > (len(q1) + len(q2)) * 2:
            return -1
        if firstSum > secondSum:
            temp = q1.popleft()
            q2.append(temp)
            firstSum -= temp
            secondSum += temp
        elif firstSum < secondSum:
            temp = q2.popleft()
            q1.append(temp)
            firstSum += temp
            secondSum -= temp
        cnt += 1
        
    return cnt