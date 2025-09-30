def solution(board):
    def bingo_check():
        O_bingo = 0
        X_bingo = 0

        # 가로
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] == 'O':
                O_bingo += 1
            if board[i][0] == board[i][1] == board[i][2] == 'X':
                X_bingo += 1

        # 세로
        for i in range(3):
            if board[0][i] == board[1][i] == board[2][i] == 'O':
                O_bingo += 1
            if board[0][i] == board[1][i] == board[2][i] == 'X':
                X_bingo += 1

        # 대각선
        if board[0][0] == board[1][1] == board[2][2] == 'O':
            O_bingo += 1
        if board[0][0] == board[1][1] == board[2][2] == 'X':
            X_bingo += 1
        if board[0][2] == board[1][1] == board[2][0] == 'O':
            O_bingo += 1
        if board[0][2] == board[1][1] == board[2][0] == 'X':
            X_bingo += 1

        return O_bingo, X_bingo

    def check():
        O_cnt = sum(row.count('O') for row in board)
        X_cnt = sum(row.count('X') for row in board)

        # 말 개수 규칙
        if not (O_cnt == X_cnt or O_cnt == X_cnt + 1):
            return False

        O_bingo, X_bingo = bingo_check()

        # 둘 다 승리 불가
        if O_bingo > 0 and X_bingo > 0:
            return False

        # O 승리 → 반드시 O가 한 수 더 많아야 함
        if O_bingo > 0 and O_cnt != X_cnt + 1:
            return False

        # X 승리 → 반드시 O와 X 개수가 같아야 함
        if X_bingo > 0 and O_cnt != X_cnt:
            return False

        return True

    return 1 if check() else 0
