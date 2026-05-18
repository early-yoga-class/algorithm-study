from collections import deque
from functools import lru_cache

def solution(h, grid, panels, seqs):
    INF = 10**15

    n = len(grid)
    m = len(grid[0])
    k = len(panels)

    # -----------------------------
    # 1. 엘리베이터 위치 찾기
    # -----------------------------
    elevator = None

    for r in range(n):
        for c in range(m):
            if grid[r][c] == '@':
                elevator = (r, c)
                break
        if elevator:
            break

    # -----------------------------
    # 2. 패널 좌표 0-index 변환
    # panels[i] = i번 패널 위치
    # -----------------------------
    panel_pos = []

    for f, r, c in panels:
        panel_pos.append((f - 1, r - 1, c - 1))

    # -----------------------------
    # 3. 2D 격자 BFS
    # 같은 층 안에서의 최단거리만 구함
    # -----------------------------
    def bfs(start_r, start_c):
        dist = [[-1] * m for _ in range(n)]
        q = deque()

        dist[start_r][start_c] = 0
        q.append((start_r, start_c))

        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        while q:
            r, c = q.popleft()

            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]

                if nr < 0 or nr >= n or nc < 0 or nc >= m:
                    continue

                if dist[nr][nc] != -1:
                    continue

                if grid[nr][nc] == '#':
                    continue

                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))

        return dist

    # -----------------------------
    # 4. 필요한 위치들에서 BFS 미리 돌리기
    # 패널 위치 k개 + 엘리베이터 위치 1개
    # -----------------------------
    points = [(r, c) for _, r, c in panel_pos]
    points.append(elevator)

    all_dist = []

    for r, c in points:
        all_dist.append(bfs(r, c))

    elevator_idx = k

    # -----------------------------
    # 5. 패널 간 이동 시간 계산
    # move_time[i][j] = i번 패널 위치에서 j번 패널 위치까지 시간
    # -----------------------------
    move_time = [[0] * k for _ in range(k)]

    for i in range(k):
        from_f, from_r, from_c = panel_pos[i]

        for j in range(k):
            to_f, to_r, to_c = panel_pos[j]

            # 같은 층이면 바로 이동
            if from_f == to_f:
                move_time[i][j] = all_dist[i][to_r][to_c]

            # 다른 층이면 현재 위치 -> 엘베 -> 층 이동 -> 목표 패널
            else:
                to_elevator = all_dist[i][elevator[0]][elevator[1]]
                from_elevator = all_dist[elevator_idx][to_r][to_c]
                floor_move = abs(from_f - to_f)

                move_time[i][j] = to_elevator + floor_move + from_elevator

    # -----------------------------
    # 6. 선행 조건을 비트마스크로 저장
    # need[x] = x번 패널을 켜기 전에 필요한 패널들의 집합
    # -----------------------------
    need = [0] * k

    for before, after in seqs:
        before -= 1
        after -= 1

        need[after] |= (1 << before)

    full_mask = (1 << k) - 1

    # -----------------------------
    # 7. DFS + DP
    # dfs(mask, cur)
    # = 현재 cur 패널 위치에 있고,
    #   mask에 포함된 패널들이 이미 켜진 상태에서
    #   나머지를 모두 켜는 최소 시간
    # -----------------------------
    @lru_cache(None)
    def dfs(mask, cur):
        if mask == full_mask:
            return 0

        best = INF

        for nxt in range(k):
            bit = 1 << nxt

            # 이미 켠 패널이면 패스
            if mask & bit:
                continue

            # 선행 조건이 아직 충족되지 않았으면 패스
            if (mask & need[nxt]) != need[nxt]:
                continue

            next_mask = mask | bit
            cost = move_time[cur][nxt] + dfs(next_mask, nxt)

            best = min(best, cost)

        return best

    # 기술자는 항상 1번 패널 위치에서 출발
    # 단, 1번 패널이 바로 활성화된 상태는 아님
    return dfs(0, 0)