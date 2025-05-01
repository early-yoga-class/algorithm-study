# 백준 1726 로봇
# bfs 풀이

# 2차원 배열 board[y][x]에서 y가 행(row), x가 열(column)인데, 수학적 좌표(x, y) 개념과 완전히 반대임을 주의하자자

from collections import deque
import sys
input = sys.stdin.readline

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# visited[y][x][d]: (y,x)에 방향 d로 온 적 있는가
visited = [[[0] * 4 for _ in range(m)] for _ in range(n)]

# 파이썬 매핑 테크닉 활용해서 방향 매핑한 것. (1=동, 2=서, 3=남, 4=북)
# d = 3 이면 리스트에 2번째에 있는 값을 리턴 해주는 느낌적인 느낌
def dir_map(d): return [0, 1, 2, 3][d-1]

sy, sx, sd = map(int, input().split())
ey, ex, ed = map(int, input().split())
sd, ed = dir_map(sd), dir_map(ed)

# BFS 시작
q = deque()
q.append((sy-1, sx-1, sd, 0))  # y, x, 방향, 명령 수
visited[sy-1][sx-1][sd] = 1

while q:
    y, x, d, cnt = q.popleft()

    # 목표 도달 시 종료
    if (y, x, d) == (ey-1, ex-1, ed):
        print(cnt)
        break

    # 1~3칸 직진
    for step in range(1, 4):
        ny = y + dy[d] * step
        nx = x + dx[d] * step

        # 범위 밖 or 벽이면 더 이상 진행 불가
        if not (0 <= ny < n and 0 <= nx < m): break
        if board[ny][nx] == 1: break

        if not visited[ny][nx][d]:
            visited[ny][nx][d] = 1
            q.append((ny, nx, d, cnt + 1))

    # 왼쪽/오른쪽 회전 (90도 두 방향)
    for nd in range(4):
        if nd == d or nd == (d ^ 1):  # 현재 방향이거나 정반대 방향은 제외
            continue
        if not visited[y][x][nd]:
            visited[y][x][nd] = 1
            q.append((y, x, nd, cnt + 1))

    # nd == (d ^ 1) : d를 이진수로 보고 맨 마지막 비트만 뒤집는 것
    # 방향	    d 값	이진수	d ^ 1 결과	    의미
    # 동	    0	    00	    1 (서)	    반대방향
    # 서	    1	    01	    0 (동)	    반대방향
    # 남  	    2	    10	    3 (북)  	반대방향
    # 북	    3	    11	    2 (남)  	반대방향
