def check(r):
    for i in range(1, N):
        if r[i - 1] == r[i]:
            if i == N - 1:
                return 1
            else:
                continue

        if abs(r[i - 1] - r[i]) > 1:
            return 0

        if r[i - 1] - r[i] == 1:
            for j in range(L):
                if i + j >= N or r[i] != r[i + j] or used[i + j]:
                    return 0
                if j == L-1 and r[i] == r[i + j]:
                    for k in range(L):
                        used[i + k] = True

        if r[i] - r[i-1] == 1:
            for j in range(L):
                if i - j - 1 < 0 or r[i - 1] != r[i - j - 1] or used[i - j - 1]:
                    return 0
                if j == L - 1 and r[i - 1] == r[i - j - 1]:
                    for k in range(L):
                        used[i - k - 1] = True

        if i == N - 1:
            return 1

T = int(input())

for tc in range(T):
    N, L = map(int, input().split())
    road = [list(map(int, input().split())) for _ in range(N)]
    res = 0

    for i in list(map(list, zip(*road))):
        road.append(i)

    for i in road:
        used = [False for _ in range(N)]
        res += check(i)

    print("#{} {}".format(tc + 1, res))