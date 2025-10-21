# 백준 1759 암호 만들기

from itertools import combinations

L, C = map(int, input().split())
secret = sorted(list(map(str, input().split())))
gather = set(["a", "e", "i", "o", "u"])

prediction = list(combinations(secret, L))
for check in prediction:
    gather_count = 0
    min_gather_count = 1
    max_gather_count = L-2
    for i in range(L):
        if check[i] in gather:
            gather_count += 1
    if min_gather_count <= gather_count <= max_gather_count:
        print(''.join(check))
    
