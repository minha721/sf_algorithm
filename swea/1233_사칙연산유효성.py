def check():
    for i in range(len(graph)-1, 0, -1):
        if len(graph[i][1]) == 2 and graph[i][1] in operator:
            return 0

        if len(graph[i]) == 4:
            leftChild = graph[int(graph[i][2])][1]
            rightChild = graph[int(graph[i][3])][1]

            if leftChild in operator or rightChild in operator:
                return 0
            else:
                if graph[i][1] == '+':
                    graph[i] = (i, int(leftChild) + int(rightChild))
                elif graph[i][1] == '-':
                    graph[i] = (i, int(leftChild) - int(rightChild))
                elif graph[i][1] == '*':
                    graph[i] = (i, int(leftChild) * int(rightChild))
                else:
                    if int(rightChild) == 0:
                        graph[i] = (i, int(leftChild) / 1)
                    else:
                        graph[i] = (i, int(leftChild) / int(rightChild))

    return 1

for tc in range(1):
    N = int(input())
    graph = [[0]]
    operator = ['+', '-', '*', '/']

    for _ in range(N):
        graph.append(list(map(str, input().split())))

    res = check()

    print("#{} {}".format(tc + 1, res))