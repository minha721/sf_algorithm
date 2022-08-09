from collections import deque

graph = [
    [9, 20, 2, 18, 11],
    [19, 1, 25, 3, 21],
    [8, 24, 10, 17, 7],
    [15, 4, 16, 5, 6],
    [12, 13, 22, 23, 14]
]

combine_graph = deque(sorted(sum(graph, [])))

visited = [[False] * 5 for i in range(5)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y):
    queue = deque([])
    queue.append([x, y])
    mTarget = 0
    graph[x][y] = combine_graph.popleft()

    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        nx = x + dx[mTarget]
        ny = y + dy[mTarget]

        visitedOne = sum(visited, [])
        if visitedOne.count(True) == 5 * 5:
            break
        else:
            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5 or visited[nx][ny] == True:
                if mTarget < 3:
                    mTarget += 1
                else:
                    mTarget = 0
                graph[x + dx[mTarget]][y + dy[mTarget]] = combine_graph.popleft()
                queue.append([x + dx[mTarget], y + dy[mTarget]])
            else:
                graph[nx][ny] = combine_graph.popleft()
                queue.append([nx, ny])

bfs(0, 0)

print(graph)