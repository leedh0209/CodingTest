T = int(input())
for test_case in range(1, T + 1):
    a = int(input())
    b = list(map(int, input().split()))
    c = set([0])
    score = 0
    for i in range(a):
        for j in list(c):
            c.add(j + b[i])

    total = len(c)
    print(f'#{test_case} {total}')