# 백준 1759 암호 만들기

from itertools import combinations

L, C = map(int, input().split())
secret = sorted(list(map(str, input().split())))
vowel = set(["a", "e", "i", "o", "u"])

prediction = list(combinations(secret, L))
for check in prediction:
    vowel_count = 0
    min_vowel_count = 1
    max_vowel_count = L-2
    for i in range(L):
        if check[i] in vowel:
            vowel_count += 1
    if min_vowel_count <= vowel_count <= max_vowel_count:
        print(''.join(check))
    
