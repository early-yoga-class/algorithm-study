import sys
from collections import deque
N = int(input())
lst = list(map(int,sys.stdin.readline().split()))
store = deque()
result = []
for i in range(len(lst)-1,-1,-1):
    if not store:
        store.append(lst[i])
        result.append(-1)
        continue

    if store:
        while store[-1] <= lst[i]:
            store.pop()
            if not store:
                break
        if not store:
            result.append(-1)
        else:
            result.append(store[-1])
        store.append(lst[i])
print(" ".join(map(str,result[::-1])))