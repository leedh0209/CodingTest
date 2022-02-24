T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for te in range(1, T + 1):
    n = int(input())
    arr = list(input().split())

    if n % 2 != 0:
        n += 1
    fir = arr[0:n // 2]
    sec = arr[n // 2:n]

    stri = ''
    for i in range(n // 2 + 1):
        if i < len(fir):
            stri += fir[i] + ' '
        if i < len(sec):
            stri += sec[i] + ' '
    print(f'#{te} {stri}')
