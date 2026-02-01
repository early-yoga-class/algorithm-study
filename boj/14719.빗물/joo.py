H, W = map(int, input().split())
heights = list(map(int, input().split()))

total_water = 0

for i in range(W):
    left_max = max(heights[:i+1])     
    right_max = max(heights[i:])      
    
    water_level = min(left_max, right_max)
    total_water += water_level - heights[i]

print(total_water)