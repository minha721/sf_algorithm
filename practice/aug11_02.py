def check(brackets):
    for i in range(N):
        if brackets[i] == '(':
            s.append(brackets[i])
        if brackets[i] == ')':
            if not s:
                return False
            s.pop()

    if s:
        return False
    else:
        return True

N = int(input())
brackets = input()
s = []
res = check(brackets)

print(res)