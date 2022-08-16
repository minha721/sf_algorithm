from collections import deque

def bfs(v):
    visited[v] = True
    queue = deque([v])

    while queue:
        x = queue.popleft()
        print(x, end=' ')

        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


# 각 노드가 연결된 정보를 표현
graph = [
    [],  # 0번 노드가 없으므로 index 0은 비워둠
    [2, 3],  # 1번 노드와 연결된 노드
    [1, 4, 5],
    [1, 7],
    [2, 6],
    [2, 6],
    [4, 5, 7],
    [3, 6]
]

# 각 노드가 방문된 정보를 표현
visited = [False]*8

bfs(1)