from collections import deque

for tc in range(1):
    V, E = map(int, input().split())
    inp = list(map(int, input().split()))
    connect = [[] for i in range(V + 1)]
    cnt = [0] * (V + 1)
    visited = [False] * (V + 1)
    q = deque()
    res = []

    for i in range(0, len(inp) - 1, 2):
        connect[inp[i + 1]].append(inp[i])

    for i in range(V + 1):
        cnt[i] = len(connect[i])

    for i in range(1, len(cnt)):
        if cnt[i] == 0:
            q.append(i)

    while q:
        s = q.popleft()
        res.append(s)

        for idx in range(len(connect)):
            for item in connect[idx]:
                if item == s and not visited[idx]:
                    cnt[idx] -= 1
                    if cnt[idx] == 0:
                        q.append(idx)
                        visited[idx] = True

    print("#{}".format(tc + 1), end=' ')
    for i in res:
        print(i, end=' ')
    print()