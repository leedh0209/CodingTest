T = 10

for test_case in range(1, 2):
    n = int(input())
    arr = list(map(int, input().split()))
    list1 = []
    total_view = 0

    for i in range(n):
        list1.append(arr[i])
        if i >= 4:
            max1 = max(list1[0], list1[1], list1[3], list1[4])
            if max1 < list1[2]:
                total_view += (list1[2] - max1)
            list1.pop(0)
    print(f'#{test_case} {total_view}')
