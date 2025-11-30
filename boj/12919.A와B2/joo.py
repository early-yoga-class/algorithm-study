import sys

sys.setrecursionlimit(10**5)

def solve():
    S = sys.stdin.readline().strip()
    T = sys.stdin.readline().strip()

    def can_transform(current_t):
        if current_t == S:
            return True
        
        if len(current_t) <= len(S):
            return False
        
        if current_t[-1] == 'A':
            if can_transform(current_t[:-1]):
                return True
        
        if current_t[0] == 'B':
            reversed_removed = current_t[::-1][:-1]
            if can_transform(reversed_removed):
                return True
                
        return False

    if can_transform(T):
        print(1)
    else:
        print(0)

if __name__ == "__main__":
    solve()