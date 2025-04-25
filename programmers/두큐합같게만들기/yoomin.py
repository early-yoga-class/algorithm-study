from collections import deque
def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    limit = len(q1)+len(q2)
    if (sum(q1)+sum(q2))%2 ==1:
        return -1
    cnt = 0
    sum1 = sum(q1)
    sum2 = sum(q2)
    while q1 and q2:
        if sum1 == sum2 or cnt >= limit*2:
            break
        if sum1>sum2:
            p = q1.popleft()
            q2.append(p)
            sum1 -= p
            sum2 += p
            cnt +=1
        else:
            p = q2.popleft()
            q1.append(p)
            sum2 -= p
            sum1 += p
            cnt+=1
    if cnt >= limit*2:
        cnt = -1
    return cnt