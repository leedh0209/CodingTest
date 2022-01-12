def power(a, b):
    if b == 1:
        return a
    return a * power(a, b - 1)


T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for te in range(1, T + 1):
    n = int(input())
    b, c = map(int, input().split())

    result = power(b, c)

    print(f'#{te} {result}')
