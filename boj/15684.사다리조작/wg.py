import sys
input = sys.stdin.readline

N, M, H = map(int, input().split())

# 보드: H x (N-1), board[r][c] == True면 r행에서 c와 c+1이 연결
board = [[False] * (N - 1) for _ in range(H)]
for _ in range(M):
    a, b = map(int, input().split())  # 1-based
    board[a - 1][b - 1] = True

def check_dest(start: int) -> int:
    cur = start  # 0..N-1
    for r in range(H):
        if cur < N - 1 and board[r][cur]:
            cur += 1
        elif cur > 0 and board[r][cur - 1]:
            cur -= 1
    return cur

def is_valid_all() -> bool:
    for s in range(N):
        if check_dest(s) != s:
            return False
    return True

def can_place(i: int, j: int) -> bool:
    # 자기 자리/좌우 인접 금지
    if board[i][j]:
        return False
    if j > 0 and board[i][j - 1]:
        return False
    if j < N - 2 and board[i][j + 1]:
        return False
    return True

answer = 4  # 0..3만 유효, 4면 불가능

# DFS 백트래킹
def dfs(count: int, x: int, y: int):
    global answer

    # 이미 더 나쁘면 컷
    if count >= answer:
        return

    # 모두 i -> i면 갱신
    if is_valid_all():
        answer = count
        return

    # 최대 3개까지만 추가
    if count == 3:
        return

    for i in range(x, H):
        start_j = y if i == x else 0
        for j in range(start_j, N - 1):
            if can_place(i, j):
                board[i][j] = True
                # 같은 행에서는 j+2부터 보면 인접충돌 검사 줄일 수 있음
                dfs(count + 1, i, j + 2)
                board[i][j] = False

# 초기 상태가 이미 정답인지 먼저 확인
if is_valid_all():
    print(0)
else:
    dfs(0, 0, 0)
    print(-1 if answer == 4 else answer)
