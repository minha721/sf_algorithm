test_case = 10

for t in range(test_case):
    T = int(input())
    N = 100
    res = -1

    graph = [list(map(int, input().split())) for _ in range(N)]
    col_graph = col_graph = list(map(list, zip(*graph)))

    for i in range(N):
        res = max(res, sum(graph[i]))
        res = max(res, sum(col_graph[i]))

    r_line = 0
    for r_point in range(N):
        r_line += graph[r_point][r_point]
    res = max(res, r_line)

    l_line = 0
    for l_point in reversed(range(N)):
        l_line += graph[l_point][l_point]
    res = max(res, l_line)

    print("#{} {}".format(t + 1, res))