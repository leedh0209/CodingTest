for test_case in range(10):
    T = int(input())
    array = [list(map(int, input().split())) for _ in range(100)]
    curr = [99, array[99].index(2)]

    for i in range(99, -1, -1):
        move = 0
        if 0 <= curr[1] - 1:
            if array[curr[0]][curr[1] - 1] == 1:
                move = -1
                while 0 <= curr[1] + move and array[curr[0]][curr[1] + move] == 1:
                    curr[1] += move
        if curr[1] + 1 < 100:
            if array[curr[0]][curr[1] + 1] == 1 and move != -1:
                move = 1
                while curr[1] + move < 100 and array[curr[0]][curr[1] + move] == 1:
                    curr[1] += move

        curr[0] -= 1
    print(f'#{T} {curr[1]}')

