import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())

arr = []
for i in range(1, 11):
    for comb in combinations(range(10), i):
        arr.append(int("".join(map(str, sorted(comb, reverse=True)))))

arr.sort()

print(arr[N] if N < len(arr) else -1)