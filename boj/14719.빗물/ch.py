import sys
input = sys.stdin.readline

H, W = map(int, input().split())

heights = list(map(int, input().split()))

ans = 0
for height in range(H, -1, -1):
    cnt = []
    for i in range(W):
        if heights[i] >= height:
           cnt.append(i)
    if len(cnt) >= 2:
        for i in range(len(cnt) - 1):
            ans += (cnt[i + 1] - cnt[i]) - 1

print(ans)