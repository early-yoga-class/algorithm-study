import sys

def calculate(cur_expr):
    cal_expr = cur_expr.replace(' ', '')
    cur_num = 0
    operator = '+'
    result = 0
    
    for num in cal_expr + '+':
        if num.isdigit():
            cur_num = cur_num *10 + int(num)
        else:
            if operator == '+':
                result += cur_num
            elif operator == '-':
                result -= cur_num
            
            cur_num = 0
            operator = num
    
    if result == 0:
        return True
    else:
        return False

def solve(cur_pos, cur_expr, n):
    if cur_pos == n:
        if calculate(cur_expr):
            print(cur_expr)
        return
    
    ops = [' ', '+', '-']
    for op in ops:
        solve(cur_pos + 1, cur_expr + op + str(cur_pos + 1), n)


t = int(sys.stdin.readline().strip())

reps = []
for _ in range(t):
    reps.append(int(sys.stdin.readline().strip()))



for rep in reps:
    
    solve(1, '1', rep)
    print()


