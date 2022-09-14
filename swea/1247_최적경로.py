from itertools import permutations

T = int(input())

for tc in range(T):
    N = int(input())
    pos = list(map(int, input().split()))

    company = []
    home = []
    customer = []

    for i in range(0, len(pos), 2):
        if i == 0:
            company.append((pos[i], pos[i + 1]))
        elif i == 2:
            home.append((pos[i], pos[i + 1]))
        else:
            customer.append((pos[i], pos[i + 1]))

    cus_list = permutations(customer, N)
    answer = 1e9

    for c in cus_list:
        order = company + list(c) + home
        dis = 0
        for i in range(N + 2):
            if dis >= answer:
                break
            if i == N + 1:
                answer = min(answer, dis)
            else:
                dis += abs(order[i][0] - order[i + 1][0]) + abs(order[i][1] - order[i + 1][1])

    print("#{} {}".format(tc + 1, answer))