from itertools import combinations

T = int(input())

for tc in range(T):
    # N은 벌통 크기
    # M은 일꾼 한 명이 선택 가능한 벌통의 수
    # C는 두명의 일꾼이 각각 채취할 수 있는 꿀의 최대 양
    N, M, C = map(int, input().split())
    honey = [list(map(int, input().split())) for _ in range(N)]

    row_max = []
    for h in honey:
        comb = list(set(list(combinations(h, M))))

        sub_comb = []
        for c in comb:
            for cnt in range(1, M + 1):
                for cc in combinations(c, cnt):
                    sub_comb.append(list(cc))

        cur_max = -1e9
        for sc in sub_comb:
            profit = 0
            if sum(sc) <= C:
                for scc in sc:
                    profit += scc**2
            cur_max = max(cur_max, profit)

        row_max.append(cur_max)

    row_max.sort(reverse=True)
    print("#{} {}".format(tc + 1, row_max[0] + row_max[1]))