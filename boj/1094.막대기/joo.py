X = int(input())
count = 0


while X > 0:
    if X & 1:  
        count += 1
    X >>= 1  

print(count)