# 백준 2056 작업

# K번 작업에 대해 선행 관계에 있는는 작업들의 번호는 모두 1 이상 (K-1) 이하
# 뒤쪽 작업이 그 전 보다 선행될 수 없다?

N = int(input())
base_task, zero = map(int, input().split())
task = [(0, base_task)]
answer = 0
for i in range(1, N):
    temp = list(map(int, input().split()))
    start = 0
    for j in range(1, temp[1]+1):
        # 지금 실행하려는 테스크의 시작시간이 선행하는 테스크(0-based)의 끝나는 시간 보다 작다면 바꾸기
        if start < task[temp[1+j]-1][1] :
            start = task[temp[1+j]-1][1]
    end = start + temp[0]
    task.append((start, end))
    if answer < end :
        answer = end
print(answer)

    