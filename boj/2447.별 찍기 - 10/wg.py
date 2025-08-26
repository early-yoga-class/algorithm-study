import sys
sys.setrecursionlimit(10**6)

def append_star(N):
  if N == 1:
    return ['*']
  stars = append_star(N // 3)
  array = []
  for S in stars:
    # 첫번째 줄
    array.append(S*3)
  for S in stars:
    # 두번째 줄(가운데 공백)
    array.append(S + ' '* (N // 3) + S)
  for S in stars:
    # 세번째 줄
    array.append(S*3)
  return array


N = int(sys.stdin.readline().strip())
print('\n'.join(append_star(N)))