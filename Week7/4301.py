T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for te in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if arr[i][j] == 0:
                arr[i][j] = 1
                if i - 2 >= 0:
                    arr[i - 2][j] = 2
                if j - 2 >= 0:
                    arr[i][j - 2] = 2
                if i + 2 < m:
                    arr[i + 2][j] = 2
                if j + 2 < n:
                    arr[i][j + 2] = 2

    total = 0
    for i in range(m):
        total += arr[i].count(1)
    print(f'#{te} {total}')