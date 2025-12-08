def solution(n, stations, w):
    ans = 0
    start = 1
    covers = 2 * w + 1
    for station in stations:
        left = station - w
        right = station + w
        if start < left: # 기지국 범위 밖일 때
            ans += (left - start + covers - 1) // covers
        start = max(start, right + 1) # 다음 시작점 갱신
    if start <= n: # 남은 칸 처리
        ans += (n - start + covers) // covers
    return ans