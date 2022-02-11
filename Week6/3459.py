T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for te in range(1, T + 1):
    num = int(input())
    sum = 1
    x = 1
    a = 1

    while sum < num:
        if a:
            x *= 4
            a = 0
        else:
            a = 1
        sum += x
    if a:
        print(f'#{te} Bob')
    else:
        print(f'#{te} Alice')