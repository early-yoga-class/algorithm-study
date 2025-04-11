from collections import deque
def solution(queue1, queue2):
    # 두 큐의 합을 구해서 middle 값 구하기
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    total = sum1 + sum2
    middle = 0
    if total % 2 == 0:
        middle = total // 2
    else:
        return -1

    for num in queue1:
        if num > middle:
            return -1
    for num in queue2:
        if num > middle:
            return -1

    count = 0
    initSize= len(queue1)
    while sum1 != sum2:
        if count > initSize * 2+1:
            count = -1
            break
        if sum1 > sum2:
            tmp = queue1.popleft()
            queue2.append(tmp)
            sum1 -= tmp
            sum2 += tmp
            count += 1
        elif sum1 < sum2:
            tmp = queue2.popleft()
            queue1.append(tmp)
            sum2 -= tmp
            sum1 += tmp
            count += 1
    answer = count
    return answer