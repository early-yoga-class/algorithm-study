def solution(word):
    N = len(word) # 원래 길이
    M = {'A':0, 'E':1, 'I':2, 'O':3, 'U':4} # 대응되는 숫자(자기 보다 앞서는 글자 수)
    L = 5 # 곱셈 처리용 수
    answer = 0
    for i in range(5):
        answer += M[word[i]] * sum(5**j for j in range(L)) + 1 # for문 돌며 자릿수별로 계산해서 더해주기
        N -= 1
        L -= 1
        if N == 0 :
            break
    return answer