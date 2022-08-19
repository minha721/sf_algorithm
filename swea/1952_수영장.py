def solve(c, s):
    global res

    if s >= res:
        return
    if c >= 12:
        res = s
    else:
        solve(c + 1, s + daily * schedule[c])
        solve(c + 1, s + month)
        solve(c + 3, s + months)

T = int(input())

for tc in range(T):
    daily, month, months, year = map(int, input().split())
    schedule = list(map(int, input().split()))

    res = year
    solve(0, 0)

    print("#{} {}".format(tc + 1, res))