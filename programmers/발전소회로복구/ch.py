from collections import deque
import heapq


def find_elevator(grid):
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == '@':
                return x, y


def bfs(grid, x, y):
    N = len(grid)
    M = len(grid[0])

    dist = [[-1] * M for _ in range(N)]
    q = deque()

    dist[x][y] = 0
    q.append((x, y))

    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    while q:
        curX, curY = q.popleft()

        for d in range(4):
            nx = curX + dirs[d][0]
            ny = curY + dirs[d][1]

            if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
            if grid[nx][ny] == '#': continue
            if dist[nx][ny] != -1: continue

            dist[nx][ny] = dist[curX][curY] + 1
            q.append((nx, ny))

    return dist


def save_panel_dist(h, grid, panels):
    k = len(panels)
    ex, ey = find_elevator(grid)

    panel_dist = [[float('inf')] * k for _ in range(k)]

    bfs_maps = []

    for f, x, y in panels:
        dist_map = bfs(grid, x - 1, y - 1)
        bfs_maps.append(dist_map)

    for i in range(k):
        f1, x1, y1 = panels[i]
        x1 -= 1
        y1 -= 1

        for j in range(k):
            f2, x2, y2 = panels[j]
            x2 -= 1
            y2 -= 1

            if i == j:
                panel_dist[i][j] = 0
                continue

            if f1 == f2:
                dist = bfs_maps[i][x2][y2]

                if dist == -1: continue

                panel_dist[i][j] = dist

            else:
                to_elevator = bfs_maps[i][ex][ey]
                from_elevator = bfs_maps[j][ex][ey]

                if to_elevator == -1 or from_elevator == -1: continue

                floor_move = abs(f1 - f2)

                panel_dist[i][j] = to_elevator + floor_move + from_elevator

    return panel_dist


def make_need_mask(k, seqs):
    need = [0] * k

    for a, b in seqs:
        a -= 1
        b -= 1
        need[b] |= (1 << a)

    return need


def get_min_time(panel_dist, need):
    n = len(panel_dist)
    full_mask = (1 << n) - 1

    dp = [[float('inf')] * n for _ in range(1 << n)]
    pq = []

    start = 0

    for first in range(n):
        if need[first] != 0: continue

        if panel_dist[start][first] == float('inf'): continue

        first_mask = 1 << first
        cost = panel_dist[start][first]

        dp[first_mask][first] = cost
        heapq.heappush(pq, (cost, first_mask, first))

    while pq:
        cost, mask, last = heapq.heappop(pq)

        if cost > dp[mask][last]: continue

        if mask == full_mask: return cost

        for next_panel in range(n):
            if mask & (1 << next_panel): continue

            if (mask & need[next_panel]) != need[next_panel]: continue

            if panel_dist[last][next_panel] == float('inf'):continue

            next_mask = mask | (1 << next_panel)
            next_cost = cost + panel_dist[last][next_panel]

            if next_cost < dp[next_mask][next_panel]:
                dp[next_mask][next_panel] = next_cost
                heapq.heappush(pq, (next_cost, next_mask, next_panel))

    return min(dp[full_mask])


def solution(h, grid, panels, seqs):
    panel_dist = save_panel_dist(h, grid, panels)
    need = make_need_mask(len(panels), seqs)

    answer = get_min_time(panel_dist, need)
    return answer