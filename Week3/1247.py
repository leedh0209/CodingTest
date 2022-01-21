def find_path(n, curr, last, array, visited):
    is_visited = visited[:]
    is_visited[curr//2] = 1
    new_total = abs(a[curr] - a[last]) + abs(a[curr + 1] - a[last + 1])

    dis = []
    for i in range(2, n - 2, 2):
        if is_visited[i//2] == 0:
            new = find_path(n, i, curr, array, is_visited)
            dis.append(new_total + new)
    if len(dis) > 0:
        return min(dis)
    else:
        return abs(a[n-2] - a[curr]) + abs(a[n-1] - a[curr + 1])


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for te in range(1, T + 1):
    n = int(input())
    a = list(map(int, input().split()))

    visited = [0 for _ in range(n + 2)]
    a[2], a[3], a[n * 2 + 2], a[n * 2 + 3] = a[n * 2 + 2], a[n * 2 + 3], a[2], a[3]

    distance = find_path(n * 2 + 4, 0, 0, a, visited)
    print(f'#{te} {distance}')

#실패에~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~