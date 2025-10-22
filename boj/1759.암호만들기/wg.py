from itertools import *
import sys
input = sys.stdin.readline


L, C = map(int, input().split())
alphabets = list(input().split())

tuple_pw_list = list(combinations(alphabets, L))

pw_list = []
vowel = ['a', 'e', 'i', 'o', 'u']

for elem in tuple_pw_list:
  elem = list(elem)
  vowel_cnt = 0
  consonant_cnt = 0

  for char in elem:
    if char in vowel:
      vowel_cnt += 1
    else:
      consonant_cnt += 1
  
  if vowel_cnt >= 1 and consonant_cnt >= 2:
    pw_list.append(''.join(sorted(elem)))


pw_list.sort()

for elem in pw_list:
  print(elem)