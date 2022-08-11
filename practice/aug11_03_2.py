def dfs(v):
    stack.append(v)

    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            print(v, end=' ')
            for i in graph[v][::-1]:
                if not visited[i]:
                    stack.append(i)

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

stack = []

# 각 노드가 방문된 정보를 표현
visited = [False] * 8

dfs(1)