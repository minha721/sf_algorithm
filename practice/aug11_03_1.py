def dfs(v):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


# 각 노드가 연결된 정보를 표현
graph = [
    [],  # 0번 노드가 없으므로 index 0은 비워둠
    [2, 3],  # 1번 노드와 연결된 노드
    [1, 4, 5],
    [1, 7],
    [2, 6],
    [2, 6],
    [4, 5, 7],
    [3, 7]
]

# 각 노드가 방문된 정보를 표현
visited = [False] * 8

dfs(1)