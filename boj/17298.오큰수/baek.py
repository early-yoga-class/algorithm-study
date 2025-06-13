from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

stack = []
result_queue = deque() 

for i in range(N-1, -1, -1):
    
    while (len(stack) != 0):
        if A[i] >= stack[-1]:
            stack.pop()
        else:
            break
    
    if len(stack) == 0:
        result_queue.appendleft(-1)
        stack.append(A[i])
    else: 
        result_queue.appendleft(stack[-1])
        stack.append(A[i])

print(" ".join(map(str, result_queue)))
