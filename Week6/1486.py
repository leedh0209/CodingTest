
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for te in range(1, T + 1):
    n, b = map(int, input().split())
    arr = list(map(int, input().split()))

    total_set = set([0])

    for i in arr:
        for j in list(total_set):
            total_set.add(j + i)

    min_total = min([i for i in list(total_set) if i >= b])
    print(f'#{te} {min_total - b}')

    #dfs 썼다가 초과해서 찬영이 코드보고 현타옴