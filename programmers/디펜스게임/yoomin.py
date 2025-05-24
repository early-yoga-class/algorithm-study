import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))

    prev0 = 0         
    prev1 = l1[0]    
    prev2 = l2[0]    

    for i in range(1, n):
        curr0 = max(prev0, prev1, prev2)
        curr1 = max(prev0, prev2) + l1[i]
        curr2 = max(prev0, prev1) + l2[i]

        prev0, prev1, prev2 = curr0, curr1, curr2

    print(max(prev0, prev1, prev2))
