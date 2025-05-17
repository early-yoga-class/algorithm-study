import heapq

def solution(n, k, enemy):
    answer = 0
    all_enemy = sum(enemy)
    if all_enemy <= n or k >= len(enemy):
        answer = len(enemy)
        return answer
    k_list = []
    for i in range(len(enemy)):
        # 무적권 모두 쓰기
        if k > 0:
            heapq.heappush(k_list, enemy[i])
            k -= 1
            answer += 1
            continue
            
        if k_list[0] < enemy[i]:
            if n-k_list[0] >= 0:
                n -= k_list[0]
                heapq.heappop(k_list)
                heapq.heappush(k_list, enemy[i])
                answer += 1
            else:
                break
        else: 
            if n - enemy[i] >= 0:
                n -= enemy[i]
                answer += 1
            else:
                break
    return answer