def visit(visited, x, y, xl, yl):
    for i in range(x, x + xl):
        visited[i][y:y + yl + 1] = [1 for _ in range(yl + 1)]


def count(arr, x, y, n):
    xl = 1
    yl = 1
    while 1:
        if x + 1 < n and arr[x + 1][y] != 0:
            xl += 1
            x += 1
        else:
            break
    while 1:
        if y + 1 < n and arr[x][y + 1] != 0:
            yl += 1
            y += 1
        else:
            break
    return xl, yl


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for te in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0 for _ in range(n)] for _ in range(n)]

    result = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0 and visited[i][j] == 0:
                xl, yl = count(arr, i, j, n)
                visit(visited, i, j, xl, yl)
                result.append([xl, yl])

    result.sort(key=lambda x: (x[0] * x[1], x[0]))

    resultstr = '#'
    resultstr += str(te) + ' ' + str(len(result)) + ' '
    for a, b in result:
        resultstr += str(a) + ' ' + str(b) + ' '
    print(resultstr)

