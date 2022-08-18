def inorder(i):
    global res

    if len(node[i]) == 4:
        # 왼쪽 -> 정점 -> 오른쪽
        inorder(int(node[i][2]))
        res += node[i][1]
        inorder(int(node[i][3]))

    elif len(node[i]) == 3:
        inorder(int(node[i][2]))
        res += node[i][1]

    else:
        res += node[i][1]

for tc in range(10):
    n = int(input())

    node = [[0]]
    for _ in range(n):
        node.append(list(map(str, input().split())))

    res = ''
    inorder(1)
    print('#{} {}'.format(tc + 1, res))