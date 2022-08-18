def preorder(i):
    global res

    if len(graph[i]) == 3:
        # 정점 -> 왼쪽 -> 오른쪽
        res += (str(graph[i][0]) + ' ')
        preorder(graph[i][1])
        preorder(graph[i][2])

    elif len(graph[i]) == 2:
        res += (str(graph[i][0]) + ' ')
        preorder(graph[i][1])

    else:
        res += (str(graph[i][0]) + ' ')

V = int(input())
graph = [[i] for i in range(V + 1)]

for i in range(V-1):
    p, c = map(int, input().split())
    graph[p].append(c)

res = ''
preorder(1)
print(res)