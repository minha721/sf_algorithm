arr = list(map(int, input().split()))
n = len(arr)
sub = []

for i in range((1<<n)):
    s = []
    for j in range(n):
        if i & (1<<j):
            s.append(arr[j])
    sub.append(s)

for i in sub:
    if len(i)!=0 and sum(i) == 0:
        print(i)