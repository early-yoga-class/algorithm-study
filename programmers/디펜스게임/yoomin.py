import heapq
def solution(n, k, enemy):
    lst = []
    heapq.heapify(lst)
    if (len(enemy) <= k):
        return len(enemy)
    
    for i in range(k):
        heapq.heappush(lst,enemy[i])
        
    
    for i in range(k,len(enemy)):
        if lst[0] < enemy[i]:
            if n >= lst[0]:
                n -= heapq.heappop(lst)
                heapq.heappush(lst,enemy[i])
            else:
                return i 
        else:
            if n >= enemy[i]:
                n -= enemy[i]
            else:
                return i
    return len(enemy)
    