# 백준 20310 타노스

A = list(''.join(map(str, input())))
for i in range(len(A)):
    A[i] = int(A[i])

cnt_0 = len(A) - sum(A)
cnt_1 = sum(A)
B = [True] * len(A)

# 1은 앞에서부터, 0은 뒤에서부터 삭제
temp = 0
for i in range(len(A)):
    if A[i] == 1 and temp < (cnt_1//2) :
        temp += 1
        B[i] = False
temp = 0
for j in range(len(A)-1, -1, -1):
    if A[j] == 0 and temp < (cnt_0//2) :
        temp += 1
        B[j] = False

result = []
for k in range(len(A)):
    if B[k] == True:
        result.append(A[k])

print(''.join(map(str, result)))