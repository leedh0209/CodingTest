T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for te in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))

    for i in range(n):
        arr[arr.index(max(arr))] -= 1
        arr[arr.index(min(arr))] += 1

    result = max(arr) - min(arr)
    print(f'#{te} {result}')