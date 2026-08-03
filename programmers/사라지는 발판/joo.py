def solution(board, aloc, bloc):
    n = len(board)
    m = len(board[0])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(cur, opponent):
        x, y = cur
        ox, oy = opponent

        if board[x][y] == 0:
            return False, 0

        win_moves = []
        lose_moves = []

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if not (0 <= nx < n and 0 <= ny < m):
                continue

            if board[nx][ny] == 0:
                continue

   
            board[x][y] = 0


            opponent_win, moves = dfs(
                (ox, oy),
                (nx, ny)
            )

     
            board[x][y] = 1

            if opponent_win:

                lose_moves.append(moves + 1)
            else:
                win_moves.append(moves + 1)

        if win_moves:
            return True, min(win_moves)

        if lose_moves:
            return False, max(lose_moves)

        return False, 0

    return dfs(tuple(aloc), tuple(bloc))[1]