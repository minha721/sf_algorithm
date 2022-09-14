T = int(input())
for tc in range(T):
    testCase, length = map(str, input().split())
    lNum = list(map(str, input().split()))
    sNum = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    cnt = []
    for i in sNum:
        cnt.append(lNum.count(i))

    pair = []
    for i in range(10):
        pair.append([sNum[i] + ' ', cnt[i]])

    print(testCase)
    for i in range(10):
        if pair[i][1] > 0:
            print(pair[i][0] * pair[i][1], end='')
    print()