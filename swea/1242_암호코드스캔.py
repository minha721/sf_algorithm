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

binary = {
    '0':'0000', '1':'0001', '2':'0010', '3':'0011',
    '4':'0100', '5':'0101', '6':'0110', '7':'0111',
    '8':'1000', '9':'1001', 'A':'1010', 'B':'1011',
    'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'
}

def check_pass(pwd):
    pwd = list(map(int, pwd))
    num = 0
    for i in range(8):
        if i % 2 == 1:
            num += (3 * pwd[i])
        else:
            num += pwd[i]

    if num % 10 == 0:
        return True
    else:
        return False

T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    arr = sorted(list(set([input().strip() for _ in range(n)])))[1:]

    visited = []
    answer = 0

    for a in arr:
        b = []
        for i in range(len(a)):
            b.append(binary[a[i]])

        b = ''.join(b).rstrip('0')
        n1, n2, n3, n4 = 0, 0, 0, 0
        password = []

        for i in range(len(b) - 1, -1, -1):
            if b[i] == '1' and n2 == 0:
                n1 += 1
            elif b[i] == '0' and n1 != 0 and n3 == 0:
                n2 += 1
            elif b[i] == '1' and n2 != 0 and n4 == 0:
                n3 += 1
            elif b[i] == '0' and n3 != 0:
                if b[i - 1] == '1':
                    r = min(n1, n2, n3)
                    password.append((ratio[n3 // r, n2 // r, n1 // r]))
                    n1, n2, n3, n4 = 0, 0, 0, 0
                    if len(password) == 8:
                        if check_pass(password):
                            if password not in visited:
                                answer += sum(password)
                                visited.append(password)
                        password = []

    print('#{} {}'.format(tc + 1, answer))