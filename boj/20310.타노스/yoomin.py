import sys

lst =  list(map(int,input()))
num_1 = sum(lst)//2
num_0 = (len(lst)-num_1*2)//2
cnt_1 = 0
cnt_0 = 0 
result = []


for i in lst:
    if i == 1:
        if cnt_1 < num_1:
            cnt_1 += 1
        else:
            result.append('1')
    else:
        if cnt_0 < num_0:
            result.append('0')
            cnt_0 += 1

print(''.join(result))
