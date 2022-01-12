T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for te in range(1, T + 1):
    n = int(input())
    array = [list(map(int, input().split())) for _ in range(100)]

    max = 0
    for i in range(100):
        row_sum = sum(array[i])
        col_sum = sum(list(zip(*array))[i])
        if max < row_sum:
            max = row_sum
        if max < col_sum:
            max = col_sum

    a = 0
    b = 0
    for i in range(100):
        a += array[i][i]
        b += array[i][99 - i]
    if max < a:
        max = a
    if max < b:
        max = b
    print(f'#{te} {max}')