for tc in range(10):
    N = int(input())
    tokens = list(map(str, input().strip()))
    formula = []  # 계산식
    stack = []
    priority = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1
    }

    # 후위 표기법으로 변환
    for i in range(len(tokens)):
        if tokens[i].isdigit():  # 숫자이면 바로 formula에 추가
            formula.append(int(tokens[i]))
        elif tokens[i] == '(':  # 여는 괄호이면 바로 stack에 추가
            stack.append(tokens[i])
        elif tokens[i] == ')':  # 닫는 괄호이면 stack에서 여는 괄호가 나올 때까지 pop을 해서 formula에 추가
            while stack[-1] != '(':
                formula.append(stack.pop())
            stack.pop()  # 괄호들은 formula에 안넣음, 그래서 여는 괄호가 나오면 그냥 pop만 한다
        else:  # 사칙 연산자가 나올 때 스택의 top에 있는 것보다 우선순위가 같거나 작으면 더 커질때까지 pop하고, 완료되면 stack에 추가
            if len(stack) == 0:
                stack.append(tokens[i])
            else:
                while len(stack) > 0:
                    if priority[stack[-1]] >= priority[tokens[i]]:
                        formula.append(stack.pop())
                    else:
                        break
                stack.append(tokens[i])

    while len(stack) != 0:
        formula.append(stack.pop())

    # 후위 표기법 계산
    for i in formula:
        if isinstance(i, str):
            num1 = stack.pop()
            num2 = stack.pop()
            if i == '+':
                stack.append(num2 + num1)
            elif i == '-':
                stack.append(num2 - num1)
            elif i == '*':
                stack.append(num2 * num1)
            elif i == '/':
                stack.append(num2 / num1)
        else:
            stack.append(i)

    print("#{} {}".format(tc + 1, stack.pop()))