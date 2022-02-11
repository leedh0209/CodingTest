T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for te in range(1, T + 1):
    n, loop = map(int, input().split())
    arr = [0 for _ in range(n)]

    for i in range(1, loop + 1):
        L, R = map(int, input().split())
        arr[L - 1:R] = [i for _ in range(R - L + 1)]

    print(f'#{te}', end=' ')
    for i in arr:
        print(i, end=' ')
    print()