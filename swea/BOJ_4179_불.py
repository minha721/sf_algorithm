# 오 나의 여신님 문제와 동일, 종료 조건이 그래프 범위 벗어 났을 때라서 그거만 다르게 처리

from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs():
    time = 0

    while jQueue:
        for _ in range(len(fQueue)):
            fy, fx = fQueue.popleft()
            for i in range(4):
                ny = fy + dy[i]
                nx = fx + dx[i]
                if 0 <= ny < R and 0 <= nx < C:
                    if graph[ny][nx] == '.' or graph[ny][nx] == 'J':
                        fQueue.append((ny, nx))
                        graph[ny][nx] = 'F'

        for _ in range(len(jQueue)):
            jy, jx = jQueue.popleft()
            for i in range(4):
                ny = jy + dy[i]
                nx = jx + dx[i]
                if not(0 <= ny < R and 0 <= nx < C):
                    return time + 1
                else:
                    if graph[ny][nx] == '.':
                        jQueue.append((ny, nx))
                        graph[ny][nx] = 'J'

        time += 1

    return 0


R, C = map(int, input().split())
graph = [list(map(str, input().strip())) for _ in range(R)]

jQueue = deque()
fQueue = deque()

for i in range(R):
    for j in range(C):
        if graph[i][j] == 'J':
            jQueue.append((i, j))
        elif graph[i][j] == 'F':
            fQueue.append((i, j))

ans = bfs()

if ans == 0:
    print("IMPOSSIBLE")
else:
    print(ans)