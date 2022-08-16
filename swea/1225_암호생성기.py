from collections import deque

for test_case in range(10):
    T = int(input())
    code = deque(map(int, input().split()))

    decrease = 0
    while True:
        if decrease == 5:
            decrease = 1
        else:
            decrease += 1
        num = code.popleft() - decrease

        if num <= 0:
            code.append(0)
            break
        else:
            code.append(num)

    print("#{}".format(T), end=' ')
    for i in code:
        print(i, end=' ')
    print()