import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

answer = []

a_idx, b_idx = 0, 0
for i in range(0, N + M):
    if a_idx >= len(A):
        answer.append(B[b_idx])
        b_idx += 1
        continue
    if b_idx >= len(B):
        answer.append(A[a_idx])
        a_idx += 1
        continue

    if A[a_idx] <= B[b_idx]:
        answer.append(A[a_idx])
        a_idx += 1
    else:
        answer.append(B[b_idx])
        b_idx += 1

print(" ".join(map(str, answer)))