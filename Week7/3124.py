def solve(route, visited):
    total = 0
    visited[route[0][0]] = 1

    while route:
        f, t, w = route.pop(0)
        if visited[t]:
            continue
        else:
            visited[t] = 1
            total += w

    return total


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for te in range(1, T + 1):
    v, e = map(int, input().split())
    route = [list(map(int, input().split())) for _ in range(e)]
    visited = [0 for _ in range(v + 1)]
    visited[0] = 1

    route.sort(key=lambda x:x[2])

    result = solve(route, visited)
    print(f'#{te} {result}')

'이거 시간내에 어떻게 하냐'