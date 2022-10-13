from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(sy, sx):
    global ans

    q = deque()
    visited = [[False] * N for _ in range(N)]

    q.append((sy, sx))
    visited[sy][sx] = True

    K = 1
    house = 0

    while q:
        # 같은 시간대의 것들(여기선 동일한 K값인 것들)을 한 번에 퍼트리기 위해 큐의 길이만큼 반복 실행
        for _ in range(len(q)):
            cy, cx = q.popleft()
            # 집이 존재하면 집 카운트 증가
            if graph[cy][cx] == 1:
                house += 1
            # 4방향에 대해 탐색
            for i in range(4):
                ny = cy + dy[i]
                nx = cx + dx[i]
                if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                    q.append((ny, nx))
                    visited[ny][nx] = True

        # cost : 운영 비용, income : 수익
        cost = K * K + (K - 1) * (K - 1)
        income = house * M
        # 이익이 있다면 서비스가 가능한 집의 최대수 비교
        if cost <= income:
            ans = max(ans, house)
        # 다음 비교를 위해 K 증가
        K += 1

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    # 모든 점에 대해 bfs 탐색 -> bfs 탐색에서 K 범위 늘려가며 값 찾음
    for i in range(N):
        for j in range(N):
            bfs(i, j)

    print("#{} {}".format(tc + 1, ans))