def dfs(x, y, cut):
    global res, visited
    res = max(res, visited[x][y])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            if mountain[x][y] > mountain[nx][ny] :
                visited[nx][ny] = visited[x][y] + 1
                dfs(nx, ny, cut)
                visited[nx][ny] = 0
            elif cut and mountain[x][y] > mountain[nx][ny] - K:
                t = mountain[nx][ny]
                mountain[nx][ny] = mountain[x][y] - 1
                visited[nx][ny] = visited[x][y] + 1
                dfs(nx, ny, cut - 1)
                visited[nx][ny] = 0
                mountain[nx][ny] = t

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]
    highest = max(sum(mountain, []))

    visited = [[0] * N for _ in range(N)]
    res = 0

    peak = [(i, j) for i in range(N) for j in range(N) if mountain[i][j] == highest]

    for x, y in peak:
        visited[x][y] = 1
        dfs(x, y, 1)
        visited[x][y] = 0

    print("#{} {}".format(tc, res))