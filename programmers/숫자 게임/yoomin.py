def solution(A, B):
    A.sort(reverse = True)
    B.sort(reverse = True)
    cnt = 0
    i = 0
    j = 0
    while(i < len(A)):
        if A[i] < B[j] :
            cnt += 1
            j += 1
        i += 1
        
    return cnt