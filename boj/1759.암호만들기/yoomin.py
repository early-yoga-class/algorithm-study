import sys
from itertools import combinations
L, C = map(int,input().split())
alphabets = sys.stdin.readline().split()
alphabets.sort()

m = ['a','e','i','o','u']

for com in combinations(alphabets,L):
    cnt = 0
    for c in com:
        if c in m:
            cnt += 1
    if 1 <= cnt <= L - 2:
        print(''.join(com))