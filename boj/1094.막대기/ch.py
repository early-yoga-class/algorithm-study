import heapq
import sys


X = int(input())
arr = [64]
sum = 64
while sum > X:
    min_stick = heapq.heappop(arr)
    cutted_stick = min_stick // 2

    if sum - cutted_stick >= X:
        sum -= cutted_stick
        heapq.heappush(arr, cutted_stick)
    else:
        heapq.heappush(arr, cutted_stick)
        heapq.heappush(arr, cutted_stick)
print(len(arr))
