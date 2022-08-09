import random

graph = [[random.randint(0, 20) for _ in range(5)] for _ in range(5)]
answer = [[0]*5 for _ in range(5)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def get_abs(x, y, num):
    res = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            res += abs(graph[nx][ny] - num)
    return res

for i in range(5):
    for j in range(5):
        answer[i][j] = get_abs(i, j, graph[i][j])

print(answer)