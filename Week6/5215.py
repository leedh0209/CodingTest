T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for te in range(1, T + 1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n):
        arr[i].append(arr[i][0]/arr[i][1])

    arr.sort(key=lambda x:-x[2])

    total = 0
    total_score = 0

    for i in range(n):
        if total + arr[i][1] < k:
            total += arr[i][1]
            total_score += arr[i][0]

    print(f'#{te} {total_score}')
    
    #재귀 안쓰고 해보려 했는데 20개중 14개만 맞고 나머지 실패