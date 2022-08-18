for tc in range(10):
    N = int(input())
    graph = [[0]]

    for _ in range(N):
        graph.append(list(map(str, input().split())))

    for i in range(len(graph)-1, 0, -1):
        if len(graph[i]) == 4:
            leftChild = int(graph[int(graph[i][2])][1])
            rightChild = int(graph[int(graph[i][3])][1])

            if graph[i][1] == '+':
                graph[i] = (i, leftChild + rightChild)
            elif graph[i][1] == '-':
                graph[i] = (i, leftChild - rightChild)
            elif graph[i][1] == '*':
                graph[i] = (i, leftChild * rightChild)
            else:
                graph[i] = (i, leftChild / rightChild)

    print("#{} {}".format(tc + 1, int(graph[1][1])))