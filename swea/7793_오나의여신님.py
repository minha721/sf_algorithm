from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs():
    time = 0
    # 수연 큐가 비어지지 않는 동안
    while qSoo:
        # 같은 시간대에 큐에 담긴 위치들을 확인해줘서 퍼트려야하기 때문에 while문 안에서 큐의 길이만큼 for문을 돌려야 함
        # 이 방법으로 하면 시간 단위로 갈 수 있는 확장된 위치를 반영
        for _ in range(len(qDevil)):
            dey, dex = qDevil.popleft()
            for i in range(4):
                ny = dey + dy[i]
                nx = dex + dx[i]
                if 0 <= ny < N and 0 <= nx < M:
                    # 악마 4방향 탐색해서 평지거나 수연이 있는 위치면 이동 가능 -> 큐에 넣고 그래프 바꿔줌
                    if graph[ny][nx] == '.' or graph[ny][nx] == 'S':
                        qDevil.append((ny, nx))
                        graph[ny][nx] = '*'

        # 같은 시간대에 큐에 담긴 위치들을 확인해줘서 퍼트려야하기 때문에 while문 안에서 큐의 길이만큼 for문을 돌려야 함
        # 이 방법으로 하면 시간 단위로 갈 수 있는 확장된 위치를 반영
        for _ in range(len(qSoo)):
            sy, sx = qSoo.popleft()
            for i in range(4):
                ny = sy + dy[i]
                nx = sx + dx[i]
                if 0 <= ny < N and 0 <= nx < M:
                    # 수연 4방향 탐색해서 평지이면 이동 가능 -> 큐에 넣고 그래프 바꿔줌
                    if graph[ny][nx] == '.':
                        qSoo.append((ny, nx))
                        graph[ny][nx] = 'S'
                    # 수연 4방향 탐색해서 여신 위치이면 time + 1값 리턴
                    elif graph[ny][nx] == 'D':
                        return time + 1

        time += 1

    return 0

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    graph = [list(map(str, input().strip())) for _ in range(N)]

    qSoo = deque()
    qDevil = deque()

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 'S':
                qSoo.append((i, j))
            elif graph[i][j] == '*':
                qDevil.append((i, j))

    ans = bfs()

    # bfs 탐색 후 0이 리턴되면 여신을 만날 수 없음 -> GAME OVER
    if ans == 0:
        print("#{} {}".format(tc + 1, "GAME OVER"))
    else:
        print("#{} {}".format(tc + 1, ans))