from collections import deque
import sys 

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
app = []
dir = []
snail = deque()
dir = deque()

n =1
status = 'r'
snail.append((1,1))
for _ in range(K):
    a, b = map(int,sys.stdin.readline().split())
    app.append((a,b))

N2 = int(sys.stdin.readline())

for _ in range(N2):
    a, b = sys.stdin.readline().split()
    dir.append((int(a),b))
########방향 전환 함수#########
def dc(status,s):
        global dir
        if status == 'l':
            if s == 'L':
                status = 'd'
            else:
                status = 'u'
        elif status == 'r':
            if s == 'L':
                status = 'u'
            else:
                status = 'd'
        elif status == 'u':
            if s == 'L':
                status = 'l'
            else:
                status = 'r'
        else:
            if s == 'L':
                status = 'r'
            else:
                status = 'l'
        return status
#############이동############
def move(a,b,status):
    global snail, app
    if status == 'l':
        if (b-1) < 1 or (a,b-1) in snail:
            return False
        snail.appendleft((a,b-1))
    elif status == 'r':
        if (b+1) > N or (a,b+1) in snail:
            return False
        snail.appendleft((a,b+1))
    elif status == 'u':
        if (a-1) < 1 or (a-1,b) in snail:
            return False
        snail.appendleft((a-1,b))
    else:
        if (a+1) > N or (a+1,b) in snail:
            return False
        snail.appendleft((a+1,b))
    ### 사과 있는지 체크 ###
    if (a,b) not in app:
        snail.pop()
    else:
        app.remove((a,b))
    return True

#############메인#############
while True:
    if dir:
        t = dir[0][0]
        s = dir[0][1]
    a,b = snail[0]
    if not move(a,b,status):
        break
    #### 방향 전환 체크 ! ####
    if n == t:
        status = dc(status,s)
        dir.popleft()
    n += 1

print(n)

