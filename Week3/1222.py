T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for te in range(1, T + 1):
    n = int(input())
    array = list(str(input()))

    stack = []

    stack.append(int(array[0]))
    for i in range(1, len(array) - 1, 2):
        if array[i] == '+':
            stack.append(int(array[i + 1]))
            stack.append(array[i])

    for i in range(len(stack)):
        if stack[i] == '+':
            new_n = stack[i - 2] + stack[i - 1]
            stack[i] = new_n
    print(f'#{te} {stack[len(stack) - 1]}')