T = int(input())

for tc in range(T):
    N = int(input())
    info = list(map(int, input().split()))

    dis = info[0:N]
    m = info[N:]

    answer = []

    # i번 자성체와 i+1번 자성체 사이의 균형점 계산
    for i in range(N-1):
        # 균형점 위치, 균형점 이동 비율 초기값
        point, ratio = dis[i], 0.5

        while True:
            # dis[i]과 dis[i+1] 사이에 균형점 위치 설정
            point += (dis[i+1] - dis[i]) * ratio
            lf, rf = 0, 0

            # 왼쪽 인력과 오른쪽 인력 계산
            for j in range(i + 1):
                lf += (m[j] / (point - dis[j]) ** 2)
            for j in range(i + 1, N):
                rf += (m[j] / (dis[j] - point) ** 2)

            # 왼쪽 인력이 작으면 왼쪽으로, 왼쪽 인력이 작으면 오른쪽으로 균형점 이동
            if lf < rf:
                ratio = -abs(ratio * 0.5)
            elif lf > rf:
                ratio = abs(ratio * 0.5)
            else:
                break

            # dis[i]나 dis[i+1] 좌표와 같아지는 경우 반복문 탈출
            # 좌표 이동량이 (1e-12)보다 작아지면 더 이상 이동이 무의미, 반복문 탈출
            if point - dis[i] < 1e-12:
                break
            if dis[i+1] - point < 1e-12:
                break
            if abs((dis[i + 1] - dis[i]) * ratio) < 1e-12:
                break

        answer.append(point)

    print("#{} {}".format(tc + 1, ' '.join('%.10f' % a for a in answer)))