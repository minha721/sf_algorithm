stack = []

for i in range(3):
    stack.append(int(input()))
    print("push {} : {}".format(i+1, stack))

for i in range(3):
    print("pop {} : {}".format(i+1, stack.pop()))