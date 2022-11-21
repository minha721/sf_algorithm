def dfs(y, x, cut):
    global res, visited
    res = max(res, visited[y][x])

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
            if mountain[y][x] > mountain[ny][nx]:
                visited[ny][nx] = visited[y][x] + 1
                dfs(ny, nx, cut)
                visited[ny][nx] = 0
            elif cut and mountain[y][x] > mountain[ny][nx] - K:
                t = mountain[ny][nx]
                mountain[ny][nx] = mountain[y][x] - 1
                visited[ny][nx] = visited[y][x] + 1
                dfs(ny, nx, cut - 1)
                visited[ny][nx] = 0
                mountain[ny][nx] = t

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]
    highest = max(sum(mountain, []))

    visited = [[0] * N for _ in range(N)]
    res = 0

    peak = [(i, j) for i in range(N) for j in range(N) if mountain[i][j] == highest]

    for y, x in peak:
        visited[y][x] = 1
        dfs(y, x, 1)
        visited[y][x] = 0

    print("#{} {}".format(tc, res))