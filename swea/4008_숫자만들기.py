T = int(input())

for tc in range(T):
    n = int(input())
    op = list(map(int, input().split()))
    number = list(map(int, input().split()))
    result = []

    answer = number[0]


    def dfs(idx):
        global answer

        if idx == n:
            result.append(answer)
            return

        for i in range(4):
            tmp = answer
            if op[i] > 0:  # 연산자가 존재하는 경우
                if i == 0:
                    answer += number[idx]
                elif i == 1:
                    answer -= number[idx]
                elif i == 2:
                    answer *= number[idx]
                else:
                    if answer < 0:
                        answer = -((-answer) // number[idx])
                    else:
                        answer //= number[idx]

                op[i] -= 1
                dfs(idx + 1)
                answer = tmp
                op[i] += 1


    dfs(1)
    print("#{} {}".format(tc + 1, max(result) - min(result)))

# 백트래킹으로 순열 고르는 방법 -> 백트래킹 정리 문서 2번 보기