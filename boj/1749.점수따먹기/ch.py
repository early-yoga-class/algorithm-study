import sys
input = sys.stdin.readline

N, M = map(int, (input().split()))
matrix = [list(map(int, input().split())) for _ in range(N)]

answer = -float('inf')

for i in range(N):
    # 행을 고정해서 세로끼리 더한 배열 생성
    col = [0] * M
    for j in range(i, N):
        for c in range(M):
            col[c] += matrix[j][c]
        # 세로를 압축한 가로 배열에서 카데인 알고리즘 사용
        local_max = col[0]
        global_max = col[0]
    
        for num in col[1:]:
            local_max = max(num, num + local_max)
            global_max = max(global_max, local_max)
    
        answer = max(global_max, answer)

print(answer)