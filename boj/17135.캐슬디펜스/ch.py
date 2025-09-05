import sys
import copy

input = sys.stdin.readline

def enemy_check(game_board):
    for i in range(N):
        for j in range(M):
            if game_board[i][j] == 1:
                return False 
    return True

def enemy_move(game_board):
    for i in range(N - 1, -1, -1):
        for j in range(M):
            if game_board[i][j] == 1:
                game_board[i][j] = 0
                if game_board[i + 1][j] != 2:
                    game_board[i + 1][j] = 1

def game_start(archers, game_board):
    global ans, D
    kill_enemy_cnt = 0

    while not enemy_check(game_board):  
        killed_enemy = set()

        for pos in archers:
            best_enemy = None
            best_dist = D + 1
            for i in range(N - 1, -1, -1):  
                for j in range(M):         
                    if game_board[i][j] != 1:
                        continue
                    dist = (N - i) + abs(j - pos) 
                    if dist > D:
                        continue
                    if dist < best_dist or (dist == best_dist and (best_enemy is None or j < best_enemy[1])):
                        best_enemy = (i, j)
                        best_dist = dist
            if best_enemy is not None:
                killed_enemy.add(best_enemy)

        kill_enemy_cnt += len(killed_enemy)
        for i, j in killed_enemy:
            game_board[i][j] = 0

        # 적 이동
        enemy_move(game_board)

    ans = max(ans, kill_enemy_cnt)

N, M, D = map(int, input().split())
init_board = [list(map(int, input().split())) for _ in range(N)]
init_board.append([2] * M) 

visited = [False] * M
ans = 0

def backtracking(archer_cnt, archers, x):
    if archer_cnt == 3:
        game_board = copy.deepcopy(init_board) 
        game_start(archers, game_board)
        return

    for i in range(x, M):
        if not visited[i]:
            visited[i] = True
            archers.append(i)
            backtracking(archer_cnt + 1, archers, i + 1)
            archers.pop()
            visited[i] = False

backtracking(0, [], 0)
print(ans)
