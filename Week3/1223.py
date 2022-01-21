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
        elif array[i] == '*':
            if stack[len(stack) - 1] == '+':
                stack.pop(len(stack) - 1)
                stack.append(int(array[i + 1]))
                stack.append(array[i])
                stack.append('+')
            else:
                stack.append(int(array[i + 1]))
                stack.append(array[i])

    a = 0
    while len(stack) > 2:
        if stack[a] == '+':
            new_n = stack[a - 2] + stack[a - 1]
            stack[a] = new_n
            stack.pop(a - 2)
            stack.pop(a - 2)
            a -= 2
        elif stack[a] == '*':
            new_n = stack[a - 2] * stack[a - 1]
            stack[a] = new_n
            stack.pop(a - 2)
            stack.pop(a - 2)
            a -= 2
        else:
            a += 1

    print(f'#{te} {stack[len(stack) - 1]}')