from itertools import *

def solution(n, weak, dist):
    answer = 1e9
# weak 배열 원형 => 선형으로 확장
    linear_weak = []
    for i in range(len(weak) * 2):
        if i < len(weak):
            linear_weak.append(weak[i])
        else:
            linear_weak.append(weak[i - len(weak)] + n)
        
# 친구 거리 dist 순열로 순서 생성(어떤 친구를 먼저 쓸지를 완전탐색)
    perm_dist = list(map(list, permutations(dist, len(dist))))
        
# 각 순열마다 탐색 진행
    for perm in perm_dist:
        # weak의 각 지점을 시작점으로
        for start in range(len(weak)): 
            count = 1
            # 첫 친구의 최대 커버 범위
            coverage = linear_weak[start] + perm[0]
            
            # weak 지점을 start 부터 검사
            for i in range(start, start + len(weak)):
                # coverage 보다 더 멀다면 새 친구 투입
                if linear_weak[i] > coverage:
                    count += 1
                    # 더이상 배치할 친구 없으면 실패
                    if count > len(perm):
                        break
                    
                    # 새로운 친구가 커버 가능한 범위 다시 설정
                    coverage = linear_weak[i] + perm[count - 1]
            # 최소 친구수 갱신
            answer = min(answer, count)
    
    if answer > len(dist):
        return -1
    else:
        return answer