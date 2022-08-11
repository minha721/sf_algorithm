T = 2

for i in range(T):
    tc = int(input())
    N, M = map(int, input().split())

    print("#{} {}".format(tc, N**M))