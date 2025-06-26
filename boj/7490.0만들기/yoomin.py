T = int(input())

def check(lst):
    sum = 0
    num = ''
    cal = '+'
    for i, val in enumerate(lst):
        if i%2 == 0:
            num += val
        else:
            if val == ' ':
                continue
            else:
                #이전 계산 부호
                if cal == '-':
                    sum -= int(num)
                    cal = val
                    num = ''
                else:
                    sum += int(num)
                    cal = val
                    num = ''
    if cal == '-':
        sum -= int(num)
        cal = val
        num = ''
    else:
        sum += int(num)
        cal = val
        num = ''

    if sum == 0:
        print(''.join(lst))


def nums(n,result):
    if n == N+1:
        check(result)
        return 
    l = [' ','+','-']
    for l_val in l:
        result.append(l_val)
        result.append(str(n))
        nums(n+1,result)
        result.pop()
        result.pop()


for _ in range(T):
    result = ['1']
    N = int(input())
    nums(2,result)
    print('')