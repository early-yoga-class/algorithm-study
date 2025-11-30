import sys

def solve():
    # 입력 받기
    N = int(sys.stdin.readline())

    if N == 1:
        print(0)
        return

    # 1단계: 에라토스테네스의 체로 소수 리스트 생성
    # N+1 크기의 리스트 생성 (True로 초기화)
    is_prime = [True] * (N + 1)
    is_prime[0] = False
    is_prime[1] = False
    # 제곱근까지만 반복 확인
    for i in range(2, int(N**0.5 + 1)):
            # i의 배수들을 모두 False로 처리
        if is_prime[i]:
            for j in range(i*i, N+1, i):
                is_prime[j] = False
    
    # 소수만 담은 리스트 생성
    primes = []
    for i, val in enumerate(is_prime):
        if val:
            primes.append(i)

    # 2단계: 투 포인터 알고리즘
    interval_sum = 0
    end = 0
    count = 0
    

    # start를 기준으로 반복 (슬라이딩 윈도우와 유사)
    for start in range(len(primes)):
        # 합이 N보다 작고, end가 범위 내에 있다면 end를 계속 증가
        while interval_sum < N and end < len(primes):
            interval_sum += primes[end]
            end +=1
        # 합이 N과 같다면 카운트 증가
        if interval_sum == N:
            count += 1

        
        # 다음 루프(start 증가)를 위해 현재 start 값을 합에서 뺌
        interval_sum -= primes[start]

    print(count)

if __name__ == "__main__":
    solve()