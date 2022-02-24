def find_days(arr, start, n):
    f = sum(arr[start:])
    newn = n - f
    if newn <= 0:
        k = 0
        for i in arr[start:]:
            n -= i
            k += 1
            if n == 0:
                break
        return k
    total = sum(arr)
    rest = newn % total
    weeks = newn // total
    if rest == 0:
        back = 0
        for i in range(6, -1, -1):
            if arr[i] == 1:
                break
            back += 1
        return len(arr[start:]) + (weeks * 7) - back
    else:
        k = 0
        for i in arr:
            rest -= i
            k += 1
            if rest == 0:
                break
        return k + len(arr[start:]) + (weeks * 7)


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for te in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))

    least = 999999999
    for i in range(7):
        if arr[i] == 1:
            result = find_days(arr, i, n)
            if result < least:
                least = result

    print(f'#{te} {least}')