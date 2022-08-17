from collections import deque

def line():
    if dir == 'up':
        g = list(map(list, zip(*graph)))
        return g
    elif dir == 'down':
        t = list(map(list, zip(*graph)))
        g = []
        for i in t:
            g.append(i[::-1])
        return g
    elif dir == 'left':
        g = graph
        return g
    else: # right
        g = []
        for i in graph:
            g.append(i[::-1])
        return g

def game():
    res = []

    for l in lines:
        while 0 in l:
            l.remove(0)

        idx = 0
        lRes = deque()

        while True:
            if idx == len(l) - 1:
                lRes.append(l[idx])
                break
            elif idx > len(l) - 1:
                break
            else:
                if l[idx] == l[idx + 1]:
                    lRes.append(l[idx] * 2)
                    idx += 2
                elif l[idx] == 0:
                    idx += 1
                else:
                    lRes.append(l[idx])
                    idx += 1

        if dir == 'right' or dir == 'down':
            lRes.reverse()

        if len(lRes) < N:
            for _ in range(N - len(lRes)):
                if dir == 'down' or dir == 'right':
                    lRes.appendleft(0)
                elif dir == 'up' or dir == 'left':
                    lRes.append(0)

        res.append(lRes)
    return res

def printRes():
    print("#{}".format(tc))
    if dir == 'left' or dir == 'right':
        for i in gameRes:
            for j in i:
                print(j, end = ' ')
            print()
    else:
        for i in range(N):
            for j in gameRes:
                print(j[i], end = ' ')
            print()

T = int(input())

for tc in range(1, T + 1):
    NN, dir = map(str, input().split())
    N = int(NN)
    graph = [list(map(int, input().split())) for _ in range(N)]

    lines = line()
    gameRes = game()
    printRes()