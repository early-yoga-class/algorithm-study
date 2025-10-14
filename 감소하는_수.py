from collections import deque

n = int(input().strip())  

result = []                       
queue = deque(range(10))          

while queue:
    num = queue.popleft()         
    result.append(num)            

    last_digit = num % 10          
    
    for next_digit in range(last_digit):
        queue.append(num * 10 + next_digit)


result.sort()                    

if n < len(result):
    print(result[n])
else:
    print(-1)
