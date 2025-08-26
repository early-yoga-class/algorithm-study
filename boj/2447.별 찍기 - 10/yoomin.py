import sys
input = sys.stdin.readline
write = sys.stdout.write

def is_blank(r, c):
    while r > 0 or c > 0:
        if r % 3 == 1 and c % 3 == 1:
            return True
        r //= 3
        c //= 3
    return False

N = int(input())
for i in range(N):
    line = []
    for j in range(N):
        line.append(' ' if is_blank(i, j) else '*')
    write(''.join(line) + '\n')
