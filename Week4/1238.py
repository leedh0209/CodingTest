T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for te in range(1, T + 1):
    a, b = map(int, input().split())
    arr = list(map(int, input().split()))
    routes = [[] for _ in range(101)]
    visited_list = set([])

    for i in range(0, a, 2):
        routes[arr[i]].append(arr[i + 1])

    last_level = routes[b]
    visited_list.add(b)
    curr_level = set([])

    moved = 1
    while moved == 1:
        for i in last_level:
            for j in routes[i]:
                if j not in visited_list:
                    curr_level.add(j)
                    visited_list.add(j)
        if len(curr_level) == 0:
            moved = 0
            break
        else:
            last_level = list(curr_level)[:]
        curr_level.clear()

    print(f'#{te} {max(last_level)}')
