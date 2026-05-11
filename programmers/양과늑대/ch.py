from collections import defaultdict

def solution(info, edges):
    max_sheep = 0
    tree = defaultdict(list)

    for parent, child in edges:
        tree[parent].append(child)

    def dfs(current, sheep, wolf, next_nodes):
        nonlocal max_sheep

        if info[current] == 0:
            sheep += 1
        else:
            wolf += 1

        if wolf >= sheep:
            return

        max_sheep = max(max_sheep, sheep)

        # 갈 수 있는 노드 추가
        possible_nodes = list(next_nodes) + list(tree[current])

        if current in possible_nodes:
            possible_nodes.remove(current)

        for next_node in possible_nodes:
            dfs(next_node, sheep, wolf, possible_nodes)

    dfs(0, 0, 0, [0])

    return max_sheep