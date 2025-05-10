n = int(input())

def count_way(n):
    if n<=2:
        return 1
    if n==3:
        return 2
    answer = [0] * (n+1)   
    answer[1], answer[2], answer[3] = 1, 1, 2
    for i in range(4, n+1):
        answer[i] = (answer[i-3] + answer[i-1]) % 1000000009
    return answer[n]

print(count_way(n))
