def solution(board):

    o_count = 0
    x_count = 0

    for row in board:
        for point in row:
            if point == 'O':
                o_count += 1
            elif point == 'X':
                x_count += 1


    # o와 x의 개수차이가 룰에 어긋나면 실패

    if not (0 <= o_count - x_count <= 1):
        return 0

    def check_winner(player):

        # 가로 체크
        for i in range(3):
            if all(board[i][j] == player for j in range(3)):
                return True

        # 세로 체크
        for j in range(3):
            if all(board[i][j] == player for i in range(3)):
                return True

        # 대각선 체크
        if all(board[i][i] == player for i in range(3)):
            return True


        if all (board[i][2-i] == player for i in range(3)):
            return True



    win_o = False
    win_x = False

    win_o = check_winner('O')
    win_x = check_winner('X')

    # o가 이겼는데 o의 o개수와 같음
    if win_o and o_count == x_count:
        return 0
    # x가 이겼는데 o의 o개수와 다름
    if win_x and o_count != x_count:
        return 0


    return 1


# 실수 케이스 먼저 생각해보기

'''
1. O와 X의 개수 차이가 0과 1이 아님
2. O가 이겼는데 X의 O개수와 같음
3. X가 이겼는데 O의 0개수와 다름
'''

# 누가 이겼는지 확인 후 실수인지 검증