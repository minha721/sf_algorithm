T = 10

for test_case in range(T):
    cnt = int(input())
    box = list(map(int, input().split()))

    for _ in range(cnt):
        high = max(box)
        low = min(box)
        i_high = box.index(high)
        i_low = box.index(low)

        box[i_high] = high - 1
        box[i_low] = low + 1

    print("#{} {}".format(test_case + 1, max(box) - min(box)))