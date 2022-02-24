def find_maxi(arr):
    max = arr[0]
    maxi = 0
    for i in range(len(arr)):
        if max <= arr[i]:
            maxi = i
            max = arr[i]
    return maxi


def find_mini(arr, n):
    min = arr[0]
    mini = 0
    for i in range(len(arr)):
        if min >= arr[i]:
            if arr[i] == 0:
                if n > 0:
                    mini = i
                    min = arr[i]
            else:
                mini = i
                min = arr[i]
    return mini


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for te in range(1, T + 1):
    arr = list(map(int, str(input())))
    maxi = arr[:]
    mini = arr[:]

    for i in range(len(arr)):
        mi = find_maxi(arr[i:])
        if mi != 0 and arr[i] != arr[i + mi]:
            maxi[i], maxi[i + mi] = maxi[i + mi], maxi[i]
            break

    for i in range(len(arr)):
        mi = find_mini(arr[i:], i)
        if mi != 0 and arr[i] != arr[i + mi]:
            mini[i], mini[i + mi] = mini[i + mi], mini[i]
            break

    maxs = ''
    mins = ''

    for i in range(len(arr)):
        maxs += str(maxi[i])
        mins += str(mini[i])

    print(f'#{te} {mins} {maxs}')
