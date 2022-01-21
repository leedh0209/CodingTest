T = int(input())



for te in range(1, T + 1):
    array = list(str(input()))

    for i in range(len(array) - 1):
        n = i + 1
        while 1:
            if n == len(array):
                break
            if array[i] == array[n]:
                array[i] = 1
                array[n] = 1
                break
            else:
                n += 1

    while 1 in array:
        array.remove(1)

    array.sort()

    if len(array) > 0:
        print(f'#{te}', end=' ')
        for i in array:
            print(i, end='')
        print()
    else:
        print(f'#{te} Good')
