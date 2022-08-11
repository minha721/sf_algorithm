for tc in range(10):
    N = int(input())
    brackets = input()
    s = []

    left = ['(', '[', '{', '<']
    right = [')', ']', '}', '>']

    for i in range(N):
        if brackets[i] in left:
            s.append(brackets[i])
        if brackets[i] in right:
            if right.index(brackets[i]) == left.index(s[-1]):
                s.pop()
            else:
                break

    if len(s) == 0:
        print("#{} {}".format(tc + 1, 1))
    else:
        print("#{} {}".format(tc + 1, 0))