T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for te in range(1, T + 1):
    points_n, link, first, second = map(int, input().split())
    arr = list(map(int, input().split()))

    first_list = set([])
    second_list = set([])
    moved = 1
    while moved:
        moved = 0
        for i in range(link * 2 - 1, -1, -2):
            if arr[i] == first:
                first_list.add(arr[i - 1])
                first = arr[i - 1]
                moved = 1
    moved = 1
    while moved:
        moved = 0
        for i in range(link * 2 - 1, -1, -2):
            if arr[i] == second:
                second_list.add(arr[i - 1])
                second = arr[i - 1]
                moved = 1

    lowest_top = list(set.intersection(first_list, second_list))[0]
    tree_list = [lowest_top]
    next_list = [0]
    total = 1

    while next_list:
        next_list.clear()
        for i in range(0, link * 2, 2):
            if arr[i] in tree_list:
                next_list.append(arr[i + 1])
        total += len(next_list)
        tree_list = next_list[:]
    print(f'#{te} {lowest_top} {total}')