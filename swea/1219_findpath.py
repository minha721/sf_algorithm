for t in range(10):
    tc, length = map(int, input().split())
    inp = list(map(int, input().split()))
    sli = []
    path = [[] for _ in range(100)]
    visited = [0] * 100

    for i in range(0, len(inp) - 1, 2):
        sli.append([inp[i], inp[i + 1]])

    for i, j in sli:
        path[i].append(j)

    stack = [0]
    while stack:
        v = stack.pop()
        if visited[v] == 0:
            visited[v] = 1
            for i in path[v]:
                if not visited[i]:
                    stack.append(i)

    print("#{} {}".format(tc, visited[99]))