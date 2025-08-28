# 백준 17135번 캐슬 디펜스

from itertools import combinations
import sys
from collections import deque
import copy

input = sys.stdin.readline

N, M, D = map(int, input().split())
original_board = [list(map(int, input().split())) for _ in range(N)]

positions = list(combinations(range(M), 3))
# 이동 방향: 좌 -> 상 -> 우
dx = [0, -1, 0]
dy = [-1, 0, 1]

def get_enemy(x, y, board):
    visited = [[False]*M for _ in range(N)]
    queue = deque()
    queue.append((x, y, 0))  # 좌표 + 거리

    while queue:
        x, y, dist = queue.popleft()
        if dist >= D: continue
        for d in range(3):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                visited[nx][ny] = True
                if board[nx][ny] == 1:
                    return (nx, ny)
                queue.append((nx, ny, dist+1))
    return None

def simulate(archers):
    temp_board = copy.deepcopy(original_board)
    kill = 0

    for _ in range(N):
        targets = set()  # 중복 공격 방지
        
        # 궁수별 공격 대상 찾기
        for col in archers:
            target = get_enemy(N, col, temp_board)
            if target:
                targets.add(target)

        # 적 제거
        for x, y in targets:
            if temp_board[x][y] == 1:
                temp_board[x][y] = 0
                kill += 1

        # 적 한 줄 아래로 이동
        temp_board.pop()
        temp_board.insert(0, [0]*M)

    return kill

max_kill = 0
for archers in positions:
    max_kill = max(max_kill, simulate(archers))

print(max_kill)