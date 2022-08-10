# for T in range(10):
#     tc = int(input())
#     target = input()
#     tLen = len(target)
#     string = input()
#     res = 0
#
#     for i in range(len(string)):
#         if target == string[i:i+tLen]:
#             res += 1
#
#     print("#{} {}".format(tc, res))

for T in range(10):
    tc = int(input())
    target = input()
    string = input()

    print("#{} {}".format(tc, string.count(target)))