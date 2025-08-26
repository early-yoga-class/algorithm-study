import sys

N = int(sys.stdin.readline().strip())

def check_star(i,j,size):
    if size == 3:
        return (i,j) != (1,1) # 가운데면 false 반환
    
    block_size = size //3 
    block_i = i // block_size
    block_j = j // block_size
    
    if block_i == 1 and block_j == 1:
        return False
    
    coordinateInBlock_i = i % block_size
    coordinateInBlock_j = j % block_size
    return check_star(coordinateInBlock_i, coordinateInBlock_j, block_size)



def solve(n):
    for i in range(n):
        for j in range(n):
            if check_star(i,j,n):
                print('*', end='')
            else:
                print(' ', end='')
        print()

solve(N)



