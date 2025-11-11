import sys
from collections import defaultdict, deque
N, d, k, c = map(int, sys.stdin.readline().split())


s = defaultdict(int)
sushies = []
max_count = 0

for i in range(N):
    sushies.append(int(input()))

for i in range(N-k,N):
    s[sushies[i]] += 1

for i in range(N):
    if i < k:
        remove = N-k+i
    else:
        remove = i-k
    add = i

    s[sushies[add]] += 1
    s[sushies[remove]] -= 1

    if s[sushies[remove]] == 0:
        del s[sushies[remove]]

    if c in s.keys():
        max_count = max(max_count,len(s))
    else:
        max_count = max(max_count,len(s) + 1)
    
print(max_count)

l = [1,2,3,3]
ls = set(l)
print(ls)
print(l)