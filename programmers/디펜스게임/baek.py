import heapq

# 그리디 + 최소 힙
def solution(n, k, enemy):
    h = []  # 무적권을 사용한 적 병력을 저장
    for i in range(len(enemy)):
        if len(h) < k:
            heapq.heappush(h, enemy[i]) # 무적권 남아있으면 사용
        elif enemy[i] > h[0]: # 지금 적이 이전 무적권 대상보다 더 크면
            n -= heapq.heappop(h)
            heapq.heappush(h, enemy[i]) # 무적권 뺏어서 지금 적에게 사용
        else:
            n -= enemy[i] # 무적권도 못 뺏으면 그냥 병사로 막기
        if n < 0: # 병사가 0보다 작아지면 실패(이전 라운드까지 성공)
            return i
    return len(enemy)