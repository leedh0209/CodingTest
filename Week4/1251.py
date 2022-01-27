
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for te in range(1, T + 1):
    a = int(input())
    xlist = list(map(int, input().split()))
    ylist = list(map(int, input().split()))
    e = float(input())

    min_dis = 999999999999999

    dist = [[0]*a for _ in range(a)]
    for i in range(a):
        for j in range(i, a):
            dist[i][j] = dist[j][i] = abs(xlist[i] - xlist[j]) + abs(ylist[i] - ylist[j])

    visited = [0 for _ in range(a)]



    print(f'#{te} {int(min_dis)}')

    #재귀 썼다가 개같이 멸망...