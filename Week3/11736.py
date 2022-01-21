T = int(input())

for te in range(1, T + 1):
    n = int(input())
    array = list(map(int, input().split()))

    result = 0

    for i in range(1, n - 1):
        max_ind = array.index(max(array[i - 1], array[i], array[i + 1]))
        min_ind = array.index(min(array[i - 1], array[i], array[i + 1]))
        if max_ind != i and min_ind != i:
            result += 1

    print(f'#{te} {result}')
