def countpath(arr, x, y, n, visited):
    count = 1
    while 1:
        visited[x][y] = 1
        if x - 1 >= 0:
            if arr[x - 1][y] == arr[x][y] + 1:
                x -= 1
                count += 1
                continue
        if y - 1 >= 0:
            if arr[x][y - 1] == arr[x][y] + 1:
                y -= 1
                count += 1
                continue
        if x + 1 < n:
            if arr[x + 1][y] == arr[x][y] + 1:
                x += 1
                count += 1
                continue
        if y + 1 < n:
            if arr[x][y + 1] == arr[x][y] + 1:
                y += 1
                count += 1
                continue
        return count


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for te in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0 for _ in range(n)] for _ in range(n)]

    result = 0
    startresult = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                count = countpath(arr, i, j, n, visited)
                if count > result:
                    result = count
                    startresult = arr[i][j]
                elif count == result:
                    if arr[i][j] < startresult:
                        startresult = arr[i][j]
    print(f'#{te} {startresult} {result}')