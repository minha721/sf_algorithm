T = int(input())
for tc in range(T):
    K = int(input())
    string = list(input())
    cnt = 0
    length = 1
    sub = []

    while True:
        if len(string) < length:
            sub = list(set(sub))
            if len(sub) < K:
                print("#{} {}".format(tc + 1, "none"))
            else:
                print("#{} {}".format(tc + 1, sorted(sub)[K - 1]))
            break
        else:
            for i in range(0, len(string) - length + 1):
                s = ''
                for j in range(length):
                    s += string[i + j]
                sub.append(s)
            cnt += len(string) - length + 1
            length += 1