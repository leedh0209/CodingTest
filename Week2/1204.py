T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for te in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))

    count = {}
    for i in arr:
        if i not in count:
            count[i] = 0
        count[i] += 1
    max_val = max(count, key=count.get)
    print(f'#{te} {max_val}')
