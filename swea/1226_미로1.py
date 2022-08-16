from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        qx, qy = q.popleft()

        for i in range(4):
            nx = qx + dx[i]
            ny = qy + dy[i]

            if nx < 1 or nx > 13 or ny < 1 or ny > 13:
                continue
            else:
                if visited[nx][ny]:
                    continue
                else:
                    if graph[nx][ny] == 1:
                        continue
                    if graph[nx][ny] == 0:
                        q.append((nx, ny))
                        visited[nx][ny] = True
                    if graph[nx][ny] == 3:
                        visited[nx][ny] = True
                        return 1

    return 0

for T in range(10):
    tc = int(input())
    graph = [list(map(int, input().strip())) for _ in range(16)]
    visited = [[False] * 16 for _ in range(16)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    res = bfs(1, 1)
    print("#{} {}".format(tc, res))