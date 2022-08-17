def dfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    stack = [(x, y)]
    room = 1

    while stack:
        sx, sy = stack.pop()

        for i in range(4):
            nx = sx + dx[i]
            ny = sy + dy[i]

            if 0 <= nx < N and 0 <= ny < N :
                if A[nx][ny] - A[sx][sy] == 1:
                    stack.append([nx, ny])
                    room += 1

    return room

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    curMax = -1
    res = []
    rooms = []

    for i in range(N):
        for j in range(N):
            roomRes = dfs(i, j)
            if curMax < roomRes:
                curMax = roomRes
                rooms.clear()
                rooms.append(A[i][j])
            elif curMax == roomRes:
                rooms.append(A[i][j])

    print("#{} {} {}".format(tc, min(rooms), curMax))
