T = int(input())

def dfs(node):
    visited[node] = True
    for n in know[node]:
        if not visited[n]:
            dfs(n)

for tc in range(T):
    N, M = map(int, input().split())

    know = [[] for _ in range(N + 1)]
    for _ in range(M):
        A, B = map(int, input().split())
        know[A].append(B)
        know[B].append(A)

    visited = [True] + [False] * N
    cnt = 0

    for i in range(1, N + 1):
        if not visited[i]:
            dfs(i)
            cnt += 1

    print("#{} {}".format(tc + 1, cnt))