import sys

input = sys.stdin.readline

N = int(input())

def recursive(N:int):
    if N == 3:
        stars = ["***", "* *", "***"]
    else:
        prev = recursive(N // 3)
        size = N // 3
        stars = []
        for i in prev:
            stars.append(i * 3)
        for i in prev:
            stars.append(i + " " * size + i)
        for i in prev:
            stars.append(i * 3)
            
    return stars
            
for i in recursive(N):
    print(i)