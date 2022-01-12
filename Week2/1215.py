T = 10

for te in range(1, 2):
    n = int(input())
    array = [list(str(input())) for _ in range(8)]

    total = 0

    for i in range(8):
        list1 = []
        for j in range(8):
            list1.append(array[i][j])
            if j >= n - 1:
                if list1 == list(reversed(list1)):
                    total += 1
                list1.pop(0)

    for i in range(8):
        list1 = []
        for j in range(8):
            list1.append(array[j][i])
            if j >= n - 1:
                if list1 == list(reversed(list1)):
                    total += 1
                list1.pop(0)

    print(f'#{te} {total}')
