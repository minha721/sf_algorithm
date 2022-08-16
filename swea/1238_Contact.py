from collections import deque

def bfs(start):
    q = deque()
    q.append((start, 1))
    res.append([start, 1])
    visited[start] = True

    while q:
        num, cnt = q.popleft()

        for i in graph[num]:
            if not visited[i]:
                q.append((i, cnt + 1))
                res.append([i, cnt + 1])
                visited[i] = True

for T in range(1, 11):
    N, S = map(int, input().split())
    inp = list(map(int, input().split()))
    length = max(inp) + 1
    visited = [False] * length
    res = []

    graph = [[] for _ in range(length)]
    for i in range(0, len(inp), 2):
        graph[inp[i]].append(inp[i + 1])

    bfs(S)

    cntMax = max(res, key=lambda x: x[1])[1]
    maxList = [num for num, cnt in res if cnt == cntMax]
    print("#{} {}".format(T, max(maxList)))