import sys

N, M, D = map(int, sys.stdin.readline().split())

board = []

for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    board.append(row)
    
    
targets = []

for r in range(N):
    for c in range(M):
        if board[r][c] == 1:
            targets.append((r,c))


def find_target(archer_pos, enemies, D):
    candidates = []
    
    for enemy in enemies:
        dist = abs(archer_pos[0] - enemy[0]) + abs(archer_pos[1] - enemy[1])
        if dist <= D:
            candidates.append((dist, enemy[1], enemy))
    
    if candidates:
        candidates.sort() 
        return candidates[0][2] 
    
    return None


def simulate(archers, original_targets, N, M, D):
    enemies = original_targets[:]
    
    total_killed = 0
    
    while enemies:
        to_kill = set()
        
        for archer_c in archers:
            archer_pos = (N, archer_c)  
            target = find_target(archer_pos, enemies, D)
            if target:
                to_kill.add(target)
        
        total_killed += len(to_kill)
        enemies = [e for e in enemies if e not in to_kill]
        
        enemies = [(r + 1, c) for r, c in enemies if r + 1 < N]
    
    return total_killed


max_killed = 0

for i in range(M - 2):
    for j in range(i + 1, M - 1):
        for k in range(j + 1, M):
            archers = [i, j, k]
            killed = simulate(archers, targets, N, M, D)
            max_killed = max(max_killed, killed)

print(max_killed)