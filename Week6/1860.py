T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for te in range(1, T + 1):
    n, m, k = map(int, input().split())
    arrive = list(map(int, input().split()))
    ma = max(arrive)
    need = [0 for _ in range(ma + 1)]
    stock = [_ // m * k for _ in range(ma + 1)]

    for i in arrive:
        need[i:] = [j + 1 for j in need[i:]]

    possible = 'Possible'
    for i in range(ma + 1):
        if need[i] > stock[i]:
            possible = 'Impossible'
            break

    print(f'#{te} {possible}')