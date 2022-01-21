T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for te in range(1, T + 1):
    n = int(input())
    array = [list(map(int, input().split())) for _ in range(n)]
    moved = [0 for _ in range(n)]
    route = [0 for _ in range(200)]

    total = 0
    is_visited = 0

    for i in range(len(array)):
        for j in range(len(array)):
            if moved[j] != 1:
                if array[j][0] % 2 == 0:
                    start = (array[j][0] // 2) - 1
                else:
                    start = ((array[j][0] + 1) // 2) - 1
                if array[j][1] % 2 == 0:
                    end = (array[j][1] // 2) - 1
                else:
                    end = ((array[j][1] + 1) // 2) - 1

                if start < end:
                    if 1 not in route[start:end + 1]:
                        for a in range(start, end + 1):
                            route[a] = 1
                        moved[j] = 1
                        is_visited = 1
                elif end < start:
                    if 1 not in route[end:start + 1]:
                        for a in range(end, start + 1):
                            route[a] = 1
                        moved[j] = 1
                        is_visited = 1
                else:
                    moved[j] = 1
        if is_visited == 1:
            total += 1
            is_visited = 0
        else:
            break
        for n in range(len(route)):
            route[n] = 0

    print(f'#{te} {total}')

#실패에~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
