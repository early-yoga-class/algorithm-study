# MTS(최소 신장 트리) -> 크루스칼 알고리즘 이용 풀이
# 싸고 연결할 수 있는 간선부터 추가(그리디 전략)하면서 사이클만 조심하면 항상 최적해(최소 비용) 보장 가능

# 유니온 파인드
# parent[x]는 "x의 부모 노드(대표자)"를 저장, 처음에는 각 노드가 자기 자신이 부모: parent[x] = x
# 트리를 구성하되, 루트는 항상 대표로 유지, find(x)는 x의 루트(대표자)를 찾는 함수
# x가 루트가 아니라면 → x의 조상 노드를 재귀로 찾고,찾은 루트를 바로 x의 부모로 저장

def solution(n, costs):

    costs.sort(key=lambda x: x[2]) # 간선 비용을 기준, 오름차순 정렬
    parent = [i for i in range(n)] # 부모 테이블 초기화
    
    def find(x): # 부모 찾기
        if parent[x] != x:
            parent[x] = find(parent[x])  # 경로 압축
        return parent[x]
    
    def union(x, y): # 합치기
        x_root = find(x)
        y_root = find(y)
        if x_root != y_root:
            parent[y_root] = x_root  # x의 부모로 y를 합침
            return True
        return False

    answer = 0

    for a, b, cost in costs: # 크루스칼 알고리즘
        if union(a, b): 
            answer += cost

    return answer