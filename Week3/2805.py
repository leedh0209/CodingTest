T = int(input())

for te in range(1, T + 1):
    n = int(input())
    array = [list(map(int, str(input()))) for _ in range(n)]

    start = n // 2
    end = start
    total = 0

    for i in range(n // 2 + 1):
        for j in range(start, end + 1):
            total += array[i][j]
        start -= 1
        end += 1
    start += 2
    end -= 2
    for i in range(n // 2 + 1, n):
        for j in range(start, end + 1):
            total += array[i][j]
        start += 1
        end -= 1
    print(f'#{te} {total}')