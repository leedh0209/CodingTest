T = int(input())

for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    answer = 1
    if a % b == 0:
        for i in range(b):
            answer *= int(a / b)
    else:
        rest = a % b
        for i in range(b):
            if rest > 0:
                answer *= (int(a / b) + 1)
                rest -= 1
            else:
                answer *= int(a / b)
    print(f'#{test_case} {answer}')
