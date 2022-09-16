from itertools import combinations

def synergy(f):
    total = 0

    for comb1, comb2 in combinations(f, 2):
        total += S[comb1][comb2] + S[comb2][comb1]

    return total

T = int(input())
for tc in range(T):
    N = int(input())
    food = [i for i in range(N)]
    S = [list(map(int, input().split())) for _ in range(N)]

    food_list = list(combinations(food, N//2))
    answer = 1e9

    for i in range(len(food_list)//2):
        taste = abs(synergy(food_list[i]) - synergy(food_list[(i+1)*(-1)]))
        answer = min(answer, taste)

    print("#{} {}".format(tc + 1, answer))