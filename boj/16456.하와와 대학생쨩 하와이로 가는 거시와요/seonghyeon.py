n = int(input())

if n <= 2:
    print(1)
else:
    num = [0 for _ in range(n)]
    num[0], num[1], num[2] = 1,1,2

    for i in range(3, n):
        num[i]=(num[i-1]+num[i-3]) % 1000000009

    print(num[n-1])