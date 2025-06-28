import sys
N, M = map(int,sys.stdin.readline().split())
l1 = list(map(int,sys.stdin.readline().split()))
l1.extend(list(map(int,sys.stdin.readline().split())))
l1.sort()
print(" ".join(list(map(str,l1))))