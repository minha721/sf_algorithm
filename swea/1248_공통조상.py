T = int(input())

for tc in range(T):
    V, E, n1, n2 = map(int, input().split())
    info = list(map(int, input().split()))
    edges = [[] for _ in range(V + 1)]

    for i in range(0, len(info), 2):
        edges[info[i + 1]].append(info[i])

    for i in range(len(edges)):
        for j in edges[i]:
            for k in edges[j]:
                if k not in edges[i]:
                    edges[i].append(k)

    n1_p = set(edges[n1])
    n2_p = set(edges[n2])
    n12_inter = list(n1_p & n2_p)[0]

    edges_sum = sum(edges, [])
    sub_cnt = edges_sum.count(n12_inter) + 1

    print("#{} {} {}".format(tc + 1, n12_inter, sub_cnt))