# 백준 7490 0 만들기

# n=끝 숫자, expr=지금까지 쌓인 수식, dix= 현수식에 넣을 숫자의 번호
def dfs(n, expr, idx):
    if idx == n:
        if eval(expr.replace(' ', '')) == 0:  # 공백은 숫자 이어붙이기 → eval로 계산 후 0이면 출력
            print(expr)
        return

    # 현재 숫자 다음에 ' ', '+', '-' 중 하나를 붙여서 재귀
    for op in [' ', '+', '-']:
        dfs(n, expr + op + str(idx + 1), idx + 1)

T = int(input())
for _ in range(T):
    N = int(input())
    dfs(N, '1', 1)
    print()
