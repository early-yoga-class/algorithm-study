import sys
input = sys.stdin.readline

N, M, H = map(int, input().split())
ladder = [[False] * (N + 1) for _ in range(H + 2)]

for _ in range(M):
    a, b = map(int, input().split())
    ladder[a][b] = True

answer = 4

def dfs(cnt, x, y):
    global answer
    
    # 조건 만족하는지 체크
    flag = True
    for start in range(1, N + 1):
        col = start
        for row in range(1, H + 1):
            if ladder[row][col]:
                col += 1
            elif ladder[row][col - 1]:
                col -= 1
        if col != start:
            flag = False
            break
    
    if flag:
        answer = min(answer, cnt)
        return
    
    if cnt >= 3 or answer <= cnt:
        return
    
    for i in range(x, H + 1):
        k = y if i == x else 1
        for j in range(k, N):
            if not ladder[i][j] and not ladder[i][j - 1] and not ladder[i][j + 1]:
                ladder[i][j] = True
                dfs(cnt + 1, i, j + 2)
                ladder[i][j] = False

dfs(0, 1, 1)
print(answer if answer <= 3 else -1)