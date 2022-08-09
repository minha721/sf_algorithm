from collections import deque

test_case = 10

for t in range(test_case):
    T = int(input())
    N = 100

    graph = [list(map(int, input().split())) for _ in range(N)]
    start = []


    def bfs(x, y):
        q = deque([(x, y)])
        flag = 0

        while q:
            x, y = q.popleft()
            print(x, y)
            if x == N - 1:
                if graph[x][y] == 2:
                    return True
                else:
                    return False
            else:
                if flag == 0:
                    if 0 <= y - 1 < N and graph[x][y - 1] == 1:
                        q.append((x, y - 1))
                        flag = 1
                        dy = -1
                    elif 0 <= y + 1 < N and graph[x][y + 1] == 1:
                        q.append((x, y + 1))
                        flag = 1
                        dy = 1
                    else:
                        q.append((x + 1, y))
                else:
                    if 0 <= x + 1 < N and graph[x + 1][y] == 1:
                        q.append((x + 1, y))
                        flag = 0
                    else:
                        q.append((x, y + dy))

    for i in range(N):
        if graph[0][i] == 1:
            start.append(i)

    for s in start:
        if bfs(0, s):
            print("#{} {}".format(t + 1, s))
            break