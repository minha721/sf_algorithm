T = int(input())

for i in range(T):
    test_case = int(input())
    score = list(map(int, input().split()))
    set_score = sorted(list(set(score)), reverse=True)
    cnt = []

    for j in set_score:
        cnt.append([j, score.count(j)])

    print("#{} {}".format(test_case, max(cnt, key=lambda x:x[1])[0]))