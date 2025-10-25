from itertools import combinations

L, C = map(int, input().split())
chars = input().split()

chars.sort()

vowels = {'a', 'e', 'i', 'o', 'u'}

for combo in combinations(chars, L):

    vowel_count = 0
    for c in combo:
        if c in vowels:
            vowel_count += 1

    consonant_count = L - vowel_count
    
    if vowel_count >= 1 and consonant_count >= 2:
        password = ''
        for char in combo:
            password += char
        print(password)