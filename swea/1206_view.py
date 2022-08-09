T = 10

for test_case in range(1, T + 1):
    answer = 0
    N = int(input())
    building = list(map(int, input().split()))
    move = [-2, -1, 1, 2]

    for i in range(N):
        cMax = -1
        for j in move:
            target = i + j
            if 0 <= target < N:
                cMax = max(cMax, building[target])
        if cMax < building[i]:
            answer += (building[i] - cMax)

    print("#{} {}".format(test_case, answer))