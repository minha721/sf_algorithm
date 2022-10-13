from collections import deque

# 상우하좌
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# 구조물에 연결 위치 표시 -> 1이면 이동 가능
hole = [
    [],
    [1, 1, 1, 1], # 상하좌우
    [1, 0, 1, 0], # 상하
    [0, 1, 0, 1], # 좌우
    [1, 1, 0, 0], # 상우
    [0, 1, 1, 0], # 하우
    [0, 0, 1, 1], # 하좌
    [1, 0, 0, 1] # 상좌
]

T = int(input())

for tc in range(T):
    N, M, R, C, L = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    q = deque()
    q.append((R, C))
    visited[R][C] = True

    time = 1
    # 큐가 비지 않을 동안 & 탈출 후 소요 시간 안에
    while q:
        if time == L:
            break
        # 같은 시간대에 각 위치들 동시에 처리하기 위해 큐의 길이만큼 반복
        for _ in range(len(q)):
            cy, cx = q.popleft()
            num = graph[cy][cx]

            # 현재 위치에서 4방향을 탐색하며 현재 위치에서 이동 가능한 방향이면 다음 위치 탐색
            for i in range(4):
                if hole[num][i] == 1:
                    ny = cy + dy[i]
                    nx = cx + dx[i]

                    # 다음 위치가 범위 내에 존재하고, 방문하지 않은 곳이고
                    if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                        # 다음 위치가 파이프가 존재하고, 다음 위치의 파이프가 현재 위치의 파이프와 이어져 있다면
                        if graph[ny][nx] > 0 and hole[graph[ny][nx]][(i+2)%4] == 1:
                            # 다음 위치 탐색 위해 큐에 넣기
                            q.append((ny, nx))
                            visited[ny][nx] = True

        # 시간 증가
        time += 1

    print("#{} {}".format(tc + 1, sum(visited, []).count(True)))