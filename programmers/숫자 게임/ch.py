def solution(A, B):
    answer = 0
    A.sort()
    B.sort()

    a = 0
    b = 0

    while a < len(A) and b < len(B):
        if B[b] > A[a]:
            a += 1
            b += 1
            answer += 1
        else:
            b += 1
              
    return answer