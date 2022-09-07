ratio = {
    (2, 1, 1): 0,
    (2, 2, 1): 1,
    (1, 2, 2): 2,
    (4, 1, 1): 3,
    (1, 3, 2): 4,
    (2, 3, 1): 5,
    (1, 1, 4): 6,
    (3, 1, 2): 7,
    (2, 1, 3): 8,
    (1, 1, 2): 9,
}

def check_pass(pwd):
    pwd = list(map(int, pwd))
    num = 0
    for i in range(8):
        if i % 2 == 0:
            num += (3 * pwd[i])
        else:
            num += pwd[i]

    return num, sum(pwd)

T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    arr = sorted(list(set([input() for _ in range(n)])))[1:]

    numbers = []
    for a in arr:
        a = a.strip('0')
        numbers.append(a)

    answer = 0
    for n in numbers:
        print(n)
        binary = format(int(n, 16), 'b')
        n1 = n2 = n3 = 0
        password = []
        for i in range(len(binary)):
            if binary[i] == '1' and n2 == 0:
                n1 += 1
            elif binary[i] == '0' and n1 != 0 and n3 == 0:
                n2 += 1
            elif binary[i] == '1' and n2 != 0:
                n3 += 1
            elif binary[i] == '0' and n3 != 0:
                r = min(n1, n2, n3)
                pw = ratio[(n1//r, n2//r, n3//r)]
                password.append(pw)
                n1 = n2 = n3 = 0

                if len(password) == 8:
                    chk, s = check_pass(password)
                    password.clear()
                    if chk % 10 == 0:
                        answer += s

    print('#{} {}'.format(tc + 1, answer))