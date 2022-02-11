T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for te in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [list(str(input())) for _ in range(n)]
    min_total = 10000000
    new_total = 0
    w_total = 0
    b_total = 0
    r_total = 0

    for w in range(n - 2):
        w_total += (m - arr[w].count('W'))
        b_total = 0
        r_total = 0
        for b in range(w + 1, n - 1):
            b_total += (m - arr[b].count('B'))
            r_total = 0
            for r in range(b + 1, n):
                r_total += (m - arr[r].count('R'))
            new_total = w_total + b_total + r_total
            if new_total < min_total:
                min_total = new_total

    print(f'#{te} {min_total}')
