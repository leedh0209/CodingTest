def count(y, x, array):
    count = 0
    for i in range(100):
        move = 0
        if 0 <= x - 1:
            if array[y][x - 1] == 1:
                move = -1
                while 0 <= x + move and array[y][x + move] == 1:
                    x += move
                    count += 1
        if x + 1 < 100:
            if array[y][x + 1] == 1 and move != -1:
                move = 1
                while x + move < 100 and array[y][x + move] == 1:
                    x += move
                    count += 1
        y += 1
        count += 1
    return count


T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for te in range(1, T + 1):
    n = int(input())
    array = [list(map(int, input().split())) for _ in range(100)]

    fast_path = 0
    fast_length = 10000
    for i in range(100):
        if array[0][i] == 1:
            length = count(0, i, array)
            if length < fast_length:
                fast_path = i
                fast_length = length
    print(f'#{te} {fast_path}')
