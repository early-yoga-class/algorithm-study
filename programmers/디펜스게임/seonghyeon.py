import heapq

def solution(n, k, enemy):
    answer = 0
    maxheap = list()

    if k >= len(enemy):
        return len(enemy)

    for i in range(len(enemy)):
        heapq.heappush(maxheap, -enemy[i])
        n -= enemy[i]

        if n < 0:
            if k == 0:
                return i
            maxEnemy = heapq.heappop(maxheap)
            n += (-maxEnemy)
            k -= 1

    return len(enemy)