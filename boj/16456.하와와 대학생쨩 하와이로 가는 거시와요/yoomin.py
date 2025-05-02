N = int(input())
if N<=2:
    a = [0]*4
else:
    a = [0]*(N+1)

a[1] = 1
a[2] = 1
a[3] = 2
if (N >=4):
    for i in range(4,N+1):
        a[i] = (a[i-3]+a[i-1])%1000000009
    print((a[N])%1000000009)
else:
    print((a[N])%1000000009)