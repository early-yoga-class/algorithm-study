# 백준 11728 배열 합치기

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = sorted(A + B)
# print(' '.join(map(str, C)))
print(*C)