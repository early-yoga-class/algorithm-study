def solution(line):
    def check_star(lineA, lineB):
        A, B, C = lineA
        D, E, F = lineB
        mod = A * E - B * D
        
        # mod가 0이면 패스
        if mod == 0: return None
    
        x = B * F - C * E
        y = C * D - A * F
        
        # 둘중 하나라도 정수가 아니면 패스
        if x % mod != 0 or y % mod != 0: return None
        
        return (x // mod, y // mod)
        
    stars = []
    for start_line in range(len(line)):
        for next_line in range(start_line + 1, len(line)):
            point = check_star(line[start_line], line[next_line])
            
            if point:
                stars.append(point)
                
    min_x = min(x for x, y in stars)
    max_x = max(x for x, y in stars)
    min_y = min(y for x, y in stars)
    max_y = max(y for x, y in stars)

    M = max_x - min_x + 1
    N = max_y - min_y + 1
    
    answer = [["."] * M for _ in range(N)]
    
    for x, y in stars:
        answer[max_y - y][x - min_x] = "*"
        
    return ["".join(_) for _ in answer]